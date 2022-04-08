const updateBtns = document.getElementsByClassName("update-cart");
const increaseDecreaseBtns = document.getElementsByClassName("in-decrease");

for (const btn of updateBtns) {
    btn.addEventListener("click", function () {
        const productId = this.dataset.product;
        const action = this.dataset.action;
        const value = this.value ? this.value : '';

        if (user === 'AnonymousUser') {
            console.log("User not logged in");
        } else {
            if (action === 'add') {
                updateUserOrder(productId, action)
            } else if (action === 'add-remove') {
                increaseDecreaseUserOrder(productId, action, value);
                location.reload();
            }

        }
    })
};

// Method for add to cart button
const updateUserOrder = (productId, action) => {
    console.log("User is valid, Sending data");
    console.log(productId, action);

    const url = 'http://127.0.0.1:8000/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action
        })
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log('data:', data)
            location.reload()
        })
};


// method for up and down arrow to increase, decrease in cart 
const increaseDecreaseUserOrder = (productId, action, value) => {
    console.log("User is valid, Sending data");
    console.log(productId, action);

    const url = 'http://127.0.0.1:8000/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action,
            'value': value
        })
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log('data:', data)
        })
};

