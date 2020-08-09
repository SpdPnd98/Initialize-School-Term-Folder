# Initialize School Term

A utility to create your current semester of studies. Feel free to pivot this for other purposes!

## Usage

1. Clone this repository
```
git clone https://github.com/SpdPnd98/Initialize-School-Term-Folder.git
```

2. Create your config files in the following format:

```
{
  "name": "YOUR_MODULE_NAME",
  "generate_weeks": 13,
  "child": [
    {
      "name": "CHILD_NAME",
      "generate_weeks": 13,
      "child":.....
    },
    {
      "name": "CHILD_NAME",
      "generate_weeks": 13,
      "child":.....
    },
    ....
  ]
}
```

- `name`: *Required*, file name for first parent
- `generate_weeks`: *Required for first parent*, used to generate  weeks in the file
- `child`: (Optional), create children directories, can be nest infinitely as files are created recursively. If the directory already exists, creation will be skipped. Each child must have a `name` element.


Please refer to the sample given in this repository.

3. Run the python script with the following commands
```
python3 Z-create_directories.py CONFIG_1.json CONFIG_2.json ...
```
You can check the contents of each json before the creation of the directory. Press `Y` to agree.


Hope this script helps with your organization for the coming school semesters!
