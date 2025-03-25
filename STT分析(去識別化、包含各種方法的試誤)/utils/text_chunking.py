"""
This is for chunking
"""
from langchain_text_splitters import RecursiveCharacterTextSplitter

class Chunking():
    """_summary_
    """
    def __init__(self, text):
        self.text = text

    def text_chunking(self, text, separators, chunk_size:int, chunk_overlap:int):
        """_summary_

        Args:
            chunk_size (int): _description_
            chunk_overlap (int): _description_
        """
        text_splitter = RecursiveCharacterTextSplitter(separators,
                                                       chunk_size=chunk_size,
                                                       chunk_overlap=chunk_overlap)
        chunking_text = text_splitter.split_text(text)

        return chunking_text