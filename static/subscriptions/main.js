// static/main.js

console.log("Sanity check!");

// Get Stripe publishable key
fetch("/subscription/config/")
.then((result) => { return result.json(); })
.then((data) => {
  const stripe = Stripe(data.publicKey);


  // you must create one of this for each subscription option you created
  let submitBtn = document.querySelector("#submitBtn");
  if (submitBtn !== null) {
    submitBtn.addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/subscription/create-checkout-session/")
      .then((result) => { return result.json(); })
      .then((data) => {
        console.log(data);
        return stripe.redirectToCheckout({sessionId: data.sessionId})
      })
      .then((res) => {
        console.log(res);
      });
    });
  }
});