API_ENDPOINT = "http://127.0.0.1:5000";

iris_form = document.getElementById("form__predict");

iris_form.addEventListener("submit", (e) => {
    e.preventDefault();

    let sepal_length = Number(e.target.sepal_length.value);
    let sepal_width = Number(e.target.sepal_width.value);
    let petal_length = Number(e.target.petal_length.value);
    let petal_width = Number(e.target.petal_width.value);

    let data = {
        sepal_length: sepal_length,
        sepal_width: sepal_width,
        petal_length: petal_length,
        petal_width: petal_width,
    };

    fetch(API_ENDPOINT, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
    .then((response) => response.json())
    .then((data) => {
        let result = document.getElementById("result");
        result.innerHTML = `<h2>Iris Type : ${data["target_name"]}</h2>`;
    })
    .catch((error) => console.error(error));
});