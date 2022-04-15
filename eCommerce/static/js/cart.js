const updateBtns = document.getElementsByClassName("update-cart");
const deleteBtns = document.getElementsByClassName("delete-item");

const continueShoppingBtn = document.getElementById("continue-shopping-btn");


// Updating cart quantity in cart and checkout and product detail page
for (const btn of updateBtns) {
    btn.addEventListener("click", function () {

        const sizeOptions = document.getElementById('select-by-size');
        const size = sizeOptions ? sizeOptions.options[sizeOptions.selectedIndex].text : '';

        const colorOptions = document.getElementById('select-by-color');
        const color = colorOptions ? colorOptions.options[colorOptions.selectedIndex].text : '';

        const qty = parseInt(document.getElementById('qty') ? document.getElementById('qty').value : 0);

        const productId = this.dataset.product;
        const action = this.dataset.action;

        // this variable is for increase and decrease quantity in cart and checkout page 
        const value = parseInt(this.value ? this.value : '');

        if (user === 'AnonymousUser') {
            console.log("User not logged in");
            alert("Please login")
            // Todo:
            // Need to add the functionality to redirect to login page 
            // and after login, the user will be redirected to the previous page
        } else {
            updateUserOrder(productId, action, value, size, color, qty)
        }
    })
};

// Method for add to cart button and quantity increase-decrease in cart
const updateUserOrder = (productId, action, value = 0, size = '', color = '', qty = 0) => {
    console.log("User is valid, Sending data");

    const url = 'https://an-nurfashion.herokuapp.com/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action,
            'value': value,
            'size': size,
            'color': color,
            'qty': qty === 0 ? qty = 1 : qty
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


// ==============for Deleting items from cart==================

for (const btn of deleteBtns) {
    btn.addEventListener("click", function () {
        const productId = this.dataset.product;
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

    const url = 'https://an-nurfashion.herokuapp.com/delete_item/';

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


