import pandas as pd
import matplotlib.pyplot as plt

def get_world_co2_emission_data(dataset):
    return dataset.query("Country == 'World'")

def get_europe_co2_emission_data(dataset):
    return dataset.query("Country == ['United Kingdom', 'France', 'Italy', 'Germany', 'Spain', 'Russia']")

def show_co2_emission(data):
    plt.plot()

    fig, ax = plt.subplots()

    ax.plot(data['Year'], data['value'])
    ax.set(xlabel='Year', ylabel='CO2 emission value',
           title='CO2 emission in Europe')
    ax.grid()

    fig.savefig("europe.png")
    plt.show()

co2_emission_dataset = pd.read_csv("../../datasets/data.csv")
co2_emission_dataset = co2_emission_dataset.rename(columns={'Entity':'Country', 'Annual CO₂ emissions (tonnes )':'value'})

if __name__ == '__main__':
    show_co2_emission(
        get_world_co2_emission_data(co2_emission_dataset)
    )