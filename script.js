async function predictDigit() {
const input = document.getElementById("imageInput")
const file = input.files[0]
    if (!file) {
        alert("Please select an image");
        return;
    }
    const formData = new FormData();
    formData.append("file", file);


       const response = await fetch(
        "http://127.0.0.1:8000/predicit",
        {
            method: "POST",
            body: formData
        }
    );
const data = await response.json();

console.log(data);

document.getElementById("result").innerText =
    `Prediction: ${data.prediction}`;}