# NASA Hackathon Keyword Search Tool

This tool allows users to search for keywords in a CSV file and retrieve relevant information based on those keywords.

## How to Use

1. **Installation**: Make sure you have Python installed on your system. Clone this repository to your local machine.

2. **Dependencies**: Install the required dependencies by running:

    ```
    pip install pandas nltk
    ```

3. **Input**: Run the script `main.py`. You will be prompted to enter your search query.

4. **Output**: The tool will search for the keywords in the specified CSV file and display the corresponding information found in the columns specified.

## Example

I have used a CSV file named `keywords.csv` with columns `Column1`, `Column2`, and `Column3`. 

```
Column1,Column2,Column3
Title,Keywords_in_Description,Databaselink
Title1,Keywords1,Databaselink1
Title2,Keywords2,Databaselink2
```

If you enter the search query "what is space exploration" in the tool, it will return:

```
Keywords: ['space', 'exploration']
The word 'space' is found in rows: 1, 2, 3, 7, 8
Wasting Away (Again) in Greenland
https://earthobservatory.nasa.gov/images/151638/wasting-away-again-in-greenland

Fires Ignite on Greek Islands
https://earthobservatory.nasa.gov/images/151628/fires-ignite-on-greek-islands

Port Stephens Bay
https://earthobservatory.nasa.gov/images/151616/port-stephens-bay

The Two Banks of Lake Nasser
nan

Snow Day in Delmarva
nan

The word 'exploration' was not found in the specified column.
```

## Contributing

Contributions are welcome! If you want to contribute to this project, please follow these steps:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.
