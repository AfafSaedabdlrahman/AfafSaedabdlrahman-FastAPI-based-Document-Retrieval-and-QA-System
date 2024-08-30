from PyPDF2 import PdfReader
import re
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)  # Initialize the PDF reader
    text = ""  # Initialize an empty string to accumulate text
    for page in reader.pages:  # Loop through each page in the PDF
        page_text = page.extract_text()  # Extract text from the page
        if page_text:
            text += page_text  # Append the extracted text to the overall text
    return text  # Return the accumulated text

# Function to preprocess text by cleaning and normalizing it
def preprocess_text(text):
    """
    Preprocess the input text by performing the following steps:
    1. Convert text to lowercase.
    2. Remove extra spaces and free lines.
    3. Remove all parentheses, commas, periods, semicolons, and colons.
    
    Args:
    text (str): The raw text to preprocess.
    
    Returns:
    str: The cleaned and preprocessed text.
    """
    text = text.lower()  # Convert text to lowercase
    text = ' '.join(text.split())  # Normalize whitespace by collapsing multiple spaces
    text = re.sub(r'[(),.;:]', '', text)  # Remove parentheses, commas, periods, semicolons, and colons
    return text  # Return the cleaned and normalized text

# Function to remove redundant chunks of text
def remove_redundancy(chunks):
    seen = set()  # Initialize a set to keep track of seen chunks
    unique_chunks = []  # Initialize a list to store unique chunks
    for chunk in chunks:  # Loop through each chunk of text
        if chunk not in seen:  # If the chunk has not been seen before
            unique_chunks.append(chunk)  # Add it to the list of unique chunks
            seen.add(chunk)  # Mark the chunk as seen
    return unique_chunks  # Return the list of unique chunks

# Function to preprocess a PDF file and store its text embeddings in the database
def preprocess_and_store_pdf(pdf_path, db):
    pdf_text = extract_text_from_pdf(pdf_path)  # Extract text from the PDF
    preprocessed_text = preprocess_text(pdf_text)  # Preprocess the extracted text
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=550, chunk_overlap=50)  # Initialize a text splitter with specific chunk size and overlap
    chunks = text_splitter.split_text(preprocessed_text)  # Split the preprocessed text into chunks
    unique_chunks = remove_redundancy(chunks)  # Remove redundant chunks
    documents = [Document(page_content=chunk) for chunk in unique_chunks]  # Create Document objects for each unique chunk
    db.add_documents(documents)  # Store the documents in the database


# Function to preprocess a query for consistency in the QA pipeline
def preprocess_query(query):
    return preprocess_text(query)  # Reuse the preprocessing function to clean and normalize the query text
