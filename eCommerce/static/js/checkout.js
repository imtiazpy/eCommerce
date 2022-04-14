// to get all the shipping form info
const shippingForm = document.getElementById('shipping-form');

// method to submit the shipping info along with order info
const submitFormData = (user, shippingForm, total) => {
    console.log('confirm order clicked')

    const userData = {
        'username': user.username,
        'email': user.email,
        'total': total
    }

    const shippingFormData = {
        'address': shippingForm.address.value,
        'city': shippingForm.city.value,
        'zipcode': shippingForm.zipcode.value,
        'phone': shippingForm.phone.value,
        'additionalInfo': shippingForm.additionalInfo.value
    }

    const url = 'https://an-nurfashion.herokuapp.com/process_order/';

    if (parseInt(total) !== 0 && shippingFormData.phone !== '') {
        fetch(url, {
            method: 'POST',
            headers: {
                //csrftoken is defined in base.html
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'userData': userData,
                'shippingFormData': shippingFormData
            })
        })
            .then(response => response.json())
            .then(data => {
                console.log("Success", data);
                alert("Order completed")
                window.location.href = "/"
            })
    } else if (parseInt(total) === 0 && shippingFormData.phone !== '') {
        // Todo: we will show some message with style other than alert for every condition
        alert("Please add some items!");
    } else if (parseInt(total) !== 0 && shippingFormData.phone === '') {
        alert('please add phone number in the shipping address form');
    } else if (parseInt(total) === 0 && shippingFormData.phone === '') {
        alert("Please add some items");
    }
};

// when confirming the order
document.getElementById('confirm-order').addEventListener('click', function (e) {
    if (user == 'AnonymousUser') {
        console.log("You're not logged in")
        // Todo:
        // add functionality to redirect to login page
        // window.location.href = "http://127.0.0.1:8000/accounts/login/"
    } else {
        // user and total are coming from "request.user" and order context 
        // both variable are declared in base.html
        submitFormData(user, shippingForm, parseFloat(total))
    }


})

