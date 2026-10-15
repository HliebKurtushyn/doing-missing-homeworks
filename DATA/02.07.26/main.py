
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# ==========================================
# Завантаження та очищення даних
# ==========================================

df = pd.read_csv("covid.csv")
df["date"] = pd.to_datetime(df["date"], errors="coerce")

numeric_columns = df.select_dtypes(include="number").columns
df[numeric_columns] = df[numeric_columns].replace([float("inf"), -float("inf")], float("nan"))

# Видаляємо рядки без ключових даних
df = df.dropna(subset=["location", "date"])
df = df.drop_duplicates(subset=["location", "date"])
df = df.sort_values(["location", "date"])

# Заповнюємо пропуски числових колонок нулями лише для показників випадків і смертей
for column in ["new_cases", "new_deaths", "new_cases_smoothed", "new_deaths_smoothed"]:
    if column in df.columns:
        df[column] = df[column].fillna(0)

df.to_csv("covid_clean.csv", index=False)
print("Очищені дані збережено у covid_clean.csv")


# ==========================================
# Завдання 2: Кореляційний аналіз
# ==========================================

candidate_columns = [
    "new_cases_smoothed",
    "new_deaths_smoothed",
    "total_cases",
    "total_deaths",
    "people_vaccinated",
    "people_fully_vaccinated",
    "population",
    "population_density",
    "median_age",
    "aged_65_older",
    "gdp_per_capita",
    "human_development_index",
]

available_columns = [c for c in candidate_columns if c in df.columns]
corr_data = df[available_columns].apply(pd.to_numeric, errors="coerce")
corr_data = corr_data.dropna(axis=1, how="all")

corr_matrix = corr_data.corr()

plt.figure(figsize=(12, 9))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("COVID-19 Correlation Matrix")
plt.tight_layout()
plt.show()

# Знаходимо найсильніші та найслабші кореляції між різними змінними
pairs = corr_matrix.where(
    ~pd.DataFrame(
        [[i == j for j in corr_matrix.columns] for i in corr_matrix.columns],
        index=corr_matrix.index,
        columns=corr_matrix.columns,
    )
).stack().reset_index()

pairs.columns = ["Variable 1", "Variable 2", "Correlation"]
pairs["Pair"] = pairs.apply(
    lambda row: tuple(sorted([row["Variable 1"], row["Variable 2"]])),
    axis=1,
)
pairs = pairs.drop_duplicates("Pair")
pairs["Abs Correlation"] = pairs["Correlation"].abs()

print("\nТри найсильші кореляції:")
print(pairs.nlargest(3, "Abs Correlation")[["Variable 1", "Variable 2", "Correlation"]])

print("\nТри найслабші кореляції:")
print(pairs.nsmallest(3, "Abs Correlation")[["Variable 1", "Variable 2", "Correlation"]])


# ==========================================
# Завдання 3: Порівняння п'яти країн
# ==========================================

countries = ["Germany", "Ukraine", "United States", "Brazil", "Australia"]
country_data = df[df["location"].isin(countries)].copy()

for column, title, ylabel in [
    ("new_cases_smoothed", "COVID-19 New Cases", "New cases (smoothed)"),
    ("new_deaths_smoothed", "COVID-19 New Deaths", "New deaths (smoothed)"),
]:
    if column not in country_data.columns:
        print(f"Колонку {column} не знайдено.")
        continue

    plt.figure(figsize=(14, 6))

    for country in countries:
        data = country_data[country_data["location"] == country]
        if not data.empty:
            plt.plot(data["date"], data[column], label=country)

    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Виводимо дати та значення пікових хвиль
for country in countries:
    data = country_data[country].dropna(subset=["new_cases_smoothed"])
    if not data.empty:
        peak = data.loc[data["new_cases_smoothed"].idxmax()]
        print(
            f"{country}: пік нових випадків "
            f"{peak['date'].date()}, значення {peak['new_cases_smoothed']:.0f}"
        )


# ==========================================
# Завдання 4: Інтерактивна вакцинація
# ==========================================

vaccination_column = "people_vaccinated"

if vaccination_column in df.columns:
    fig = go.Figure()

    for country in countries:
        data = df[df["location"] == country].dropna(
            subset=[vaccination_column]
        )

        if not data.empty:
            fig.add_trace(go.Scatter(
                x=data["date"],
                y=data[vaccination_column],
                mode="lines",
                name=country,
            ))

    fig.update_layout(
        title="COVID-19 Vaccination by Country",
        xaxis_title="Date",
        yaxis_title="People vaccinated",
        hovermode="x unified",
    )

    fig.show()
else:
    print(f"Колонку {vaccination_column} не знайдено.")
