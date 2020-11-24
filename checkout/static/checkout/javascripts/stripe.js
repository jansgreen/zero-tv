// A reference to Stripe.js initialized with your real test publishable API key.

/* THIS CODE COME FROM BOUTIQUE ADO AND STRIPE DOCUMENTATIONS, IT WAS ADJUSTED TO ZERO-TV PROJECT*/
var PublicKey = $("#id_stripe_public_key").text().slice(1, -1);
var clientSecret = $("#id_stripe_client_secret").text().slice(1, -1);
var intent = $("#id_intent").text().slice(1, -1);
var stripe = Stripe(PublicKey);
var elements = stripe.elements();
var style = {
  base: {
    width:"200px",
    color: "#3a7ba0",
    fontFamily: "Arial, sans-serif",
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {},
 
  },
  invalid: {
    fontFamily: "Arial, sans-serif",
    color: "#fa755a",
  },

  class: {
    focus: 'is-focused',
    empty: 'is-empty',
  },

};
var card = elements.create("card", { style: style });
card.mount("#card-element");

card.addEventListener("change", function (event) {
  var errorDiv = document.getElementById("card-error");
  if (event.error) {
    var html = `<span class ="icon" role="alert"> <i class="fa fa-times"></i></span> <span>${event.error.message}</span>`;
    $(errorDiv).html(html);
  } else {
    errorDiv.textContent = "";
  }
});
/* form submit*/

var form = document.getElementById("payment-form");

form.addEventListener("submit", function (ev) {
  ev.preventDefault();
  card.update({ disabled: true });
  $("#button-submit").attr("disabled", true);
  $("#payment-form").fadeToggle(100);
  $("#loading-overlay").fadeToggle(100);

  var saveInfo = Boolean($("#id-save-info").attr("checked"));
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  var postData = {
    csrfmiddlewaretoken: csrfToken,
    client_Secret: clientSecret,
    saveInfo: saveInfo,
  };

  var url = "/checkout/cache_checkout/";
  $.post(url, postData).done(function() {
    console.log("entrando en profundidad");
    stripe
      .confirmCardPayment(intent, {
        payment_method: {
          card: card,
          billing_details: {
            name: $.trim(form.full_name.value),
            email: $.trim(form.email.value),
            phone: $.trim(form.phone_number.value),
            address: {
              line1: $.trim(form.street_address.value),
              city: $.trim(form.town_or_city.value),
              state: $.trim(form.county.value),
              postal_code: $.trim(form.postcade.value),
              country: $.trim(form.country.value),
            },
          },
        },
        shipping: {
          name: $.trim(form.full_name.value),
          phone: $.trim(form.phone_number.value),
          address: {
            line1: $.trim(form.street_address.value),
            city: $.trim(form.town_or_city.value),
            state: $.trim(form.county.value),
            postal_code: $.trim(form.postcade.value),
            country: $.trim(form.country.value),
          }
        },
      })
      .then(function (result) {
        if (result.error) {
          var errorDiv = document.getElementById("card-error");
          var html = `<span class ="icon" role="alert"> <i class="fa fa-times"></i></span> <span>${result.error.message}</span>`;
          $(errorDiv).html(html);
          $("#payment-form").fadeToggle(100);
          $("#loading-overlay").fadeToggle(100);
          card.update({ disabled: true });
          $("#submit-button").attr("disabled", true);
        } else {
          if (result.paymentIntent.status === "succeeded") {
            form.submit();
            // Complete payment when the submit button is clicked
          }
        }
      });
  }).fail(function () {
    location.reload();
});
});
