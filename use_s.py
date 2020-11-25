from duc_preprocess import duc2001, duc2002

# Writes single document 2001 summarization data to duc2001_output.
# import spacy
# print(spacy.__version__)
duc2001_path="DUC2001_Summarization_Documents.tgz"
duc2001_output="DATA"
duc2001.preprocess_sds(duc2001_output, nist_data_path=duc2001_path)

# # Writes single document 2002 summarization data to duc2002_output.
# duc2002_path="PATH/TO/DUC2002_Summarization_Document.tgz"
# duc2002_test_data="PATH/TO/DUC2002_test_data.tar.gz"
# duc2002_output="PATH/TO/WRITE/DUC2002/DATA"
# duc2002.preprocess_sds(
#     duc2002_output, 
#     nist_document_data_path=duc2002_path,
#     nist_summary_data_path=duc2002_test_data)