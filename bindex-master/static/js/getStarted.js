$(document).ready(function() {

    var tabContents = {}

    $(".tab-pane").each(function(index) {
        tabContents[index] = this
    })

    function checkIfChecked(item) {
        if (!$('input[type="radio"][name=' + item + ']:checked').length) {
            $('#error-message').text('Please select one')
            isValid = false;
        } else {
            $('#error-message').empty()
            isValid = true;
        }
    }

    function checkIfNumber(item) {
        if (!$('input[type="number"][name=' + item + ']').val()) {
            $('#error-message').text('Please enter a number')
            isValid = false;
        } else {
            $('#error-message').empty()
            isValid = true;
        }
    }

    $('#rootwizard').bootstrapWizard({
        onNext: function(tab, navigation, index) {
            var nextIndex = index - 1

            $(tabContents[nextIndex]).find("input").each(function() {
                if ($(this).is(':radio')) {
                    var radioName = $(this).attr('name');
                    checkIfChecked(radioName)
                } else {
                    var numberName = $(this).attr('name');
                    checkIfNumber(numberName)
                }

            });

        },
        onPrevious: function(tab, navigation, index) {
            $('#error-message').empty();
        },
        onTabShow: function(tab, navigation, index) {
            var $total = navigation.find('li').length;
            var $current = index + 1;
            var $percent = ($current / $total) * 100;
            $('#rootwizard .progress-bar').css({
                width: $percent + '%'
            });
        }
    });



    //form submission

    $('#rootwizard .finish').click(function(e) {
        var form = $('#questions-form');
        var formData = $(form).serializeArray();
        $('.shell-container').empty();
        $('.shell-container').append('<div style="text-align: center;margin-top: 10em;margin-bottom: 10em;"><i class="fa fa-spinner fa-spin" style="font-size: 100px;color:#488b08"></i></div>')
        $.ajax({
            url: "/form/get-started/risk-submission",
            data: formData,
            type: 'POST',
            success: function(response) {
                console.log(response);
            }
        });
    });


    // canvas.onclick = function(evt) {
    //     var activePoints = myNewChart.getElementsAtEvent(evt);
    //     if (activePoints[0]) {
    //         var chartData = activePoints[0]['_chart'].config.data;
    //         var idx = activePoints[0]['_index'];
    //
    //         var label = chartData.labels[idx];
    //         var value = chartData.datasets[0].data[idx];
    //
    //         var url = "http://example.com/?label=" + label + "&value=" + value;
    //         console.log(url);
    //         alert(url);
    //     }
    // };


});
