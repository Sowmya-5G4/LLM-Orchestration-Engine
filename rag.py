from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader


def setup_rag():
    loader = TextLoader("docs/contract.txt")
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    embeddings = OllamaEmbeddings(model="llama3")
    vectorstore = FAISS.from_documents(docs, embeddings)

    return vectorstore


vectorstore = setup_rag()


def retrieve(query: str) -> str:
    docs = vectorstore.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in docs])
