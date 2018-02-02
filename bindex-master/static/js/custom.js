


//calculator

function formatCurrency(n, currency) {
    n = parseFloat(n)
    return currency + " " + n.toFixed(2).replace(/(\d)(?=(\d{3})+\.)/g, "$1,");
}

$("#calc-submit").click(function() {

    var amountValue = $("#calc-amount").val();
    $('.projected-chart-section').append('<div class="colorlib-load"></div>');

    var high = 1
    var med = 2
    var low = 3
    var btc = 4
    var sp = 5

    $.ajax({
        url: '/api/v1/get-calculation?amount=' + amountValue,
        type: 'GET',
        success: function(result) {
            $('.colorlib-load').fadeOut('slow', function() {
                $(this).remove();
            });
            // projectedData(high, med, low, btc, sp);
            $("#calc-inputs").html("<p>You could make up to " + formatCurrency(result, "$") + " in 6 months!</p>");
            $("#calc-submit").replaceWith('<a href="#"><button data-toggle="modal" data-target="#investModal" style="cursor:pointer" type="submit" class="submit">Invest</button></a>');
        }
    });

});

$(window).on('load', function() {
    $.ajax({
        url: '/api/v1/get-top-three',
        type: 'GET',
        success: function(result) {
            $('#bitcoin-chart-ticker').html(formatCurrency(result['btc_price'], "$"));
            $('#sp-chart-ticker').html(formatCurrency(result['sp_price'], "$"));
        }
    });

});
