import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

iris = pd.read_csv("iris.csv")

# LabelEncoder для цільової категоріальної змінної
le = LabelEncoder()
iris["Species_encoded"] = le.fit_transform(iris["Species"])

# OneHotEncoder для категоріальної ознаки
ohe = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
encoded = ohe.fit_transform(iris[["Species"]])

encoded_df = pd.DataFrame(
    encoded,
    columns=ohe.get_feature_names_out(["Species"]),
    index=iris.index
)

iris = pd.concat([iris, encoded_df], axis=1)

print("LabelEncoder:")
print(iris[["Species", "Species_encoded"]].head())

print("\nOneHotEncoder:")
print(encoded_df.head())