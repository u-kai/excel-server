# Excel Server

## How to Run

execute below command ad project root dir

```
uvicorn main:app --reload
```

or

```
./app-start.sh
```
## write-contents api example

```shell
curl -X POST -H "Content-Type:application/json" -d '{
    "filename":"test-write.xlsx","contents":[["Hello","World"],["A","B","C"]]
}' localhost:8000/write-contents
```

## read-cell api example

```shell
curl -X POST -H "Content-Type:application/json" -d '{
    "filename":"test.xlsx","cell":"A1"
}' localhost:8000/read-cell

# response
# {"index":"A1","value":"hello world"}
```

## read-cells api example
```shell
curl -X POST -H "Content-Type:application/json" -d '{
    "filename":"test.xlsx","start_cell":"A1","end_cell":"C3"
}' localhost:8000/read-cells
```
```json
// response
{
    "start":"A1",
    "end":"C3",
    "cells":[
        [
            "hello world",null,null
        ],
        [
            "A","B","C"
        ],
        [
            "A","B","C"
        ],
    ]
}
```
