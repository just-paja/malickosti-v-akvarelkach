$(function() {
  var updatePaymentMethodAvailability = function() {
    var selectedDeliveryMethod = $('#orderDeliveryMethods input:checked');

    if (selectedDeliveryMethod.length) {
      var paymentMethodsAllowed;
      var paymentMethods = $('#orderPaymentMethods');

      try {
        paymentMethodsAllowed = JSON.parse(selectedDeliveryMethod.attr('data-payment-methods'));
      } catch(e) {
        paymentMethodsAllowed = [];
      }

      paymentMethods.find('input').each(function(index, input) {
        var jqInput = $(input);

        if (paymentMethodsAllowed.indexOf(parseInt(input.value)) !== -1) {
          jqInput.prop('disabled', false);
        } else {
          if (jqInput.prop('checked')) {
            jqInput.prop('checked', false);
          }
          jqInput.prop('disabled', true);
        }
      });
    }
  };

  $('#orderDeliveryMethods input').change(updatePaymentMethodAvailability);
  updatePaymentMethodAvailability();
});
