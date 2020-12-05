/*for this code I fallwo the intruction in bootstrap*/

$('.carousel').carousel({
  interval: 2000
})

var action = intent.next_action;
if (action && action.type === 'redirect_to_url') {
  window.location = action.redirect_to_url.url;
}

$('#navbar-example2').tooltip({
  sanitizeFn: function (content) {
    return DOMPurify.sanitize(content)
  }
})