from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(
    texts: list[str],
    chunk_size: int = 500,
    chunk_overlap: int = 50,
) -> list[str]:
    """
    Split long documents into smaller chunks.

    Args:
        texts: List of documents.
        chunk_size: Maximum characters.
        chunk_overlap: Overlap between chunks.

    Returns:
        List of chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    chunks = []

    for text in texts:
        chunks.extend(splitter.split_text(text))

    return chunks