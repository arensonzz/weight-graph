# How to use it?
1. Create a properly formatted csv file containing dates and people weights at that day.<br/>
    1. There's an example csv file in the repo. Csv file must have the same format as that file.<br/>
    2. When filling the date column, date format is day/month/year<br/>
    3. There can be as many person names as you would like.<br/>
    4. If a person didn't measure his/her weight that day you can write null into his/her column.<br/>
2. From command-line run:<br/>
    *python weight_graph.py weight_data.csv person_name*<br/>
    **Ex:** python weight_graph.py example_csv_file.csv alex<br/>

# Dependencies
* python3<br/>
* matplotlib<br/>
    * To install run: *pip3 install matplotlib*
