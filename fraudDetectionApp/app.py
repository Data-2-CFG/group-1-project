from config import *
from model import *

st.write("""
# Explore machine learning models for fraud detection
Which one is the best?        
         """)
         
dataset_name = st.sidebar.selectbox("Select Dataset",
                                   ("Creditcard Fraud Detection", "")
                                   )


clf_name = st.sidebar.selectbox("Select Classifier", 
                                      ("Decision Tree", "Logistic Regression")
                                      )

df = load_dataset(dataset_name)

st.subheader("{} Dataset".format(dataset_name))
st.write(df.head(5))
st.write("Shape of the Dataset", df.shape)
st.write("Number of Classes", len(df["is_fraud"].unique()))


st.subheader("{} Classifier".format(clf_name))

df_clean = clean_dataset(df)
df_encode = encode_dataset(df_clean)

X, y = divide_dataset(df_encode)
y_test, y_pred = fit_model(clf_name, X, y)
accuracy, precision, recall = evaluate_model(y_test, y_pred)

st.write("Accuracy: ",accuracy)
st.write("Precision: ", precision)
st.write("Recall: ", recall)

st.subheader("Confusion Matrix")
plot_matrix(y_test, y_pred)


    
    
