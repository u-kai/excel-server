#[derive(serde::Deserialize, serde::Serialize)]
struct WriteContents<'a> {
    filename: &'a str,
    contents: Vec<Vec<&'a str>>,
    start_cell: &'a str,
}
#[tokio::main]
async fn main() {
    let contents = vec![
        vec!["A", "B", "C"],
        vec!["Hello", "World"],
        vec![
            r#"todo
1.eat
2.coding
3.sleep"#,
        ],
    ];
    let filename = "result.xlsx";
    let start_cell = "A1";
    let write_content = WriteContents {
        filename,
        contents,
        start_cell,
    };
    let port = std::env::args()
        .skip(1)
        .next()
        .unwrap_or("5051".to_string());
    let client = reqwest::Client::new();
    let response = client
        .post(format!("http://localhost:{}/write-contents", port))
        .body(serde_json::to_string(&write_content).unwrap())
        .send()
        .await
        .unwrap()
        .text()
        .await
        .unwrap();
    println!("{}", response);
}
