import streamlit as st
import pandas as pd
import os

# Cache our data
@st.cache(allow_output_mutation=True)
def load_df():
    # 현재 스크립트의 디렉토리를 가져오기
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # CSV 파일의 절대 경로 생성
    csv_file_path = os.path.join(script_directory, "/Users/youngseo/Downloads/streamlit-labs-main/강의자료/data/titanic.csv")

    # CSV 파일 읽기
    df = pd.read_csv(csv_file_path)

    survival_options = df.Survived.unique()
    p_class_options = df.Pclass.unique()
    sex_options = df.Sex.unique()
    embark_options = df.Embarked.unique()

    min_fare = df.Fare.min()
    max_fare = df.Fare.max()
    min_age = df.Age.min()
    max_age = df.Age.max()

    return df, survival_options, p_class_options, sex_options, embark_options, min_fare, max_fare, min_age, max_age

def check_rows(column, options):
    return df.loc[df[column].isin(options)]  # 'res'를 'df'로 변경

st.title("Demo DataFrame Query App")
df, survival_options, p_class_options, sex_options, embark_options, min_fare, max_fare, min_age, max_age = load_df()

name_query = st.text_input("String match for Name")
cols = st.columns(4)
survival = cols[0].multiselect("Survived", survival_options)
p_class = cols[1].multiselect("Passenger Class", p_class_options)
sex = cols[2].multiselect("Sex", sex_options)
embark = cols[3].multiselect("Embarked", embark_options)

range_cols = st.columns(3)
min_fare_range, max_fare_range = range_cols[0].slider("Lowest Fare", float(min_fare), float(max_fare), [float(min_fare), float(max_fare)])
min_age_range, max_age_range = range_cols[2].slider("Lowest Age", float(min_age), float(max_age), [float(min_age), float(max_age)])

# 'res' 대신 'df'를 사용하여 새로운 DataFrame 생성
res = df.copy()

if name_query != "":
    res = res.loc[res.Name.str.contains(name_query)]

if survival:
    res = check_rows("Survived", survival)

if p_class:
    res = check_rows("Pclass", p_class)

if sex:
    res = check_rows("Sex", sex)

if embark:
    res = check_rows("Embarked", embark)

if range_cols[0].checkbox("Use Fare Range"):
    res = res.loc[(res.Fare > min_fare_range) & (res.Fare < max_fare_range)]

if range_cols[2].checkbox("Use Age Range"):
    res = res.loc[(res.Age > min_age_range) & (res.Age < max_age_range)]

removal_columns = st.multiselect("Select Columns to Remove", df.columns.tolist())

for column in removal_columns:
    res = res.drop(column, axis=1)

st.write(res)
