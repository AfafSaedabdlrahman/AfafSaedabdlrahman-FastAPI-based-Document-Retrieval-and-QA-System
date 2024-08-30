from langchain_community.llms import Ollama
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_community.vectorstores import PGVector

# Function to perform reasoning and generate a response based on a query
def reason_and_act(query, vector_store, qa_chain):
    # Perform similarity search in the vector store to find relevant documents
    similar_docs = vector_store.similarity_search(query, k=3)
    
    # Combine the content of the similar documents into a single context string
    context = " ".join([doc.page_content for doc in similar_docs])
    
    # Invoke the QA chain to generate a response using the context and the original query
    response = qa_chain.invoke({
        "input_documents": similar_docs,
        "question": query
    })
    
    # Return the generated response or a default message if no answer is found
    return response.get('output_text', 'No answer found.')

# Function to initialize the Retrieval-Augmented Generation (RAG) system
def initialize_rag_system():
    # Set up the embedding function using a pre-trained Hugging Face model
    embedding_function = HuggingFaceEmbeddings(model_name='sentence-transformers/paraphrase-MiniLM-L6-v2')
    
    # Initialize the vector store for storing document embeddings using PostgreSQL with pgvector
    db = PGVector(
        collection_name='documents',  # The name of the collection in the vector store
        connection_string='postgresql+psycopg2://postgres:test@localhost:5432/vector_db',  # Connection string to the PostgreSQL database
        embedding_function=embedding_function  # The function used to generate embeddings
    )
    
    # Initialize the language model (LLM) using Ollama with the specified model
    llm = Ollama(model="smollm",temperature=0)
    
    # Create a prompt template for the QA chain, defining how the context and question are presented to the model
    qna_prompt = PromptTemplate(
        input_variables=["context", "question"],  # Variables to be filled in the template
        template="Based on the following context, answer the question.\n\nContext: {context}\n\nQuestion: {question}\nAnswer:"  # The template for the prompt
    )
    
    # Load the question-answering (QA) chain, combining the language model and the prompt template
    qa_chain = load_qa_chain(llm, chain_type="stuff", prompt=qna_prompt)
    
    # Return the initialized vector store and QA chain for use in the application
    return db, qa_chain
