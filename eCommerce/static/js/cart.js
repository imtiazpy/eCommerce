const updateBtns = document.getElementsByClassName("update-cart");
const deleteBtns = document.getElementsByClassName("delete-item");

for (const btn of updateBtns) {
    btn.addEventListener("click", function () {
        const productId = this.dataset.product;
        const action = this.dataset.action;
        const value = parseInt(this.value ? this.value : '');

        if (user === 'AnonymousUser') {
            console.log("User not logged in");
        } else {
            updateUserOrder(productId, action, value)
        }
    })
};

// Method for add to cart button and quantity increase-decrease in cart
const updateUserOrder = (productId, action, value = 0) => {
    console.log("User is valid, Sending data");
    console.log(productId, action, value);

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
            location.reload()
        })
};


// for Deleting items from cart

for (const btn of deleteBtns) {
    btn.addEventListener("click", function () {
        const productId = this.dataset.product;
        // const action = this.dataset.action;
        // const value = parseInt(this.value ? this.value : '');
        if (user === 'AnonymousUser') {
            console.log("User not logged in");
        } else {
            deleteUserOrder(productId)
        }
    })
};

const deleteUserOrder = (productId) => {
    console.log("User is valid, Deleting Item");
    console.log(productId);

    const url = 'http://127.0.0.1:8000/delete_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId,
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

