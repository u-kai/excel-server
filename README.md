# Excel Server

## How to Run
uvicorn main:app --reload

## write-contents api example
```shell
curl -X POST -H "Content-Type:application/json" -d '{
    "filename":"test-write.xlsx","contents":[["Hello","World"],["A","B","C"]]
}' localhost:8000/write-contents
```