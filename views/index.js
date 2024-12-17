document.getElementById("offer-form").addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(event.target);

    const offerData = {
        category_name: formData.get("category_name"),
        service_name: formData.get("service_name"),
        offer_stars: parseFloat(formData.get("offer_stars")),
        offer_raters: parseInt(formData.get("offer_raters")),
        offer_response_time: formData.get("offer_response_time"),
        offer_buyers: parseInt(formData.get("offer_buyers")),
        pending: parseInt(formData.get("pending")),
        duration: formData.get("duration"),
        reviews: parseInt(formData.get("reviews")),
        available_additions: parseInt(formData.get("available_additions")),
        additions_price: parseFloat(formData.get("additions_price")),
        owner_verified: formData.get("owner_verified") === "on",
        owner_level: formData.get("owner_level"),
        owner_stars: parseFloat(formData.get("owner_stars")),
        owner_raters: parseInt(formData.get("owner_raters")),
        owner_completion_rate: parseFloat(formData.get("owner_completion_rate")),
        owner_services: parseInt(formData.get("owner_services")),
        owner_customers: parseInt(formData.get("owner_customers")),
        owner_response_time: formData.get("owner_response_time")
    };

    const resultContainer = document.getElementById("result");

    resultContainer.classList.add("show");

    fetch("http://0.0.0.0:10000/offer/", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(offerData)
    }).then(response => response.json()).then(data => {
        if (data.status === 201) {
            fetchPrice();
        } else {
            alert("Error: " + data.message);
        }
    });
});

function fetchPrice() {
    const offerId = 0;

    fetch(`http://0.0.0.0:10000/offer/${offerId}`).then(response => response.json()).then(data => {
        document.getElementById("result").textContent = data.message;
    });
}

document.getElementById("owner_verified").addEventListener("change", function () {
    const label = document.getElementById("owner_verified_label");
    if (this.checked) {
        label.textContent = "هوية موثقة";
        label.classList.remove("btn-outline-danger");
        label.classList.add("btn-outline-success");
    } else {
        label.textContent = "هوية غير موثقة";
        label.classList.remove("btn-outline-success");
        label.classList.add("btn-outline-danger");
    }
});

