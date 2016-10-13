$(function(){ 
	var selectingToAccount = false;
	var selectingFromAccount = false;

	var idOfSelectedToAccount;
	var idOfSelectedFromAccount;
	var balanceAmount;

	/* ========== Set Style for Transfer Table ========== */
	$(".status").each(function() {
		parent = $(this).parent();
		if ($(this).text() == "cancelled") {
			parent.css('background-color', '#ECC3BF');
		} else if ($(this).text() == "pending") {
			parent.css('background-color', '#FFFACD');
		} else if ($(this).text() == "executed") {
			parent.css('background-color', '#BCED91');
		}
	});

	/* ========== Selecting To Account Button ========== */

	$("#selectTransferToBtn").click(function() {
		$(".account").filter(function() {
				return !(isSelected($(this)));
			}).css(selectingAccountsCss);

		selectingToAccount = true;
		selectingFromAccount = false;
	});


	/* ========== Selecting From Account Button ========== */

	$("#selectTransferFromBtn").click(function() {
		$(".account").filter(function() {
				return !(isSelected($(this)));
			}).css(selectingAccountsCss);

		selectingFromAccount = true;
		selectingToAccount = false;
	});


	/* ========== Account Selection ========== */

	var resetSelections = {
		'selectedToAccount': false,
		'selectedFromAccount': false
	};

	// set all accounts as not selected
	$(".account").data(resetSelections);
	
	$(".account").click(function() {
		var isToAccountSelected = $(this).data('selectedToAccount');
		var isFromAccountSelected = $(this).data('selectedFromAccount')
		var selected = isToAccountSelected || isFromAccountSelected;
		
		if (selectingToAccount) {
			// store the id of this account
			idOfSelectedToAccount = $(this).attr('id')

			// update the UI to show which account was selected
			$("#transferToAccount").text($(this).find(".nickname").text());

			// reset all borders on accounts
			$(".account").filter(function() {
				return !(isFromSelected($(this)));
			}).css(emptyBorder);

			// clear any other To Account selections that have been made
			resetToData();

			// mark this account as selected
			$(this).data('selectedToAccount', true);
			$("#toAccount").val(idOfSelectedToAccount);

			// if the From Account is selected, overwrite it
			if ($(this).data('selectedFromAccount') == true) {
				$(this).data('selectedFromAccount', false);
				idOfSelectedFromAccount = undefined;
				$("#transferFromAccount").text("");
				$("#fromAccount").val("");
			}
			
			// add a border to the selected account to show it's selected
			$('#' + idOfSelectedToAccount).css(selectedToAccountCss);

			// no longer selecting a To Account
			selectingToAccount = false;
		} else if (selectingFromAccount) {
			// store the id of this account
			idOfSelectedFromAccount = $(this).attr('id')

			// update the UI to show which account was selected
			$("#transferFromAccount").text($(this).find(".nickname").text());

			// reset all borders on accounts
			$(".account").filter(function() {
				return !(isToSelected($(this)))
			}).css(emptyBorder);

			// clear any other From Account selections that have been made
			resetFromData();

			// mark this account as selected
			$(this).data('selectedFromAccount', true);
			$("#fromAccount").val(idOfSelectedFromAccount);
			
			// if the To Account is selected, overwrite it
			if ($(this).data('selectedToAccount') == true) {
				$(this).data('selectedToAccount', false);
				idOfSelectedToAccount = undefined;
				$("#transferToAccount").text("");
				$("#toAccount").val("");
			}

			// add a border to the selected account to show it's selected
			$('#' + idOfSelectedFromAccount).css(selectedFromAccountCss);

			// no longer selecting a From Account
			selectingFromAccount = false;
		} else if (selected) {
			if (isToAccountSelected) {
				$("#transferToAccount").text("");
			} else if (isFromAccountSelected) {
				$("#transferFromAccount").text("");
			}

			$(this).data(resetSelections)
			$(this).css(emptyBorder);
		}
	});


	/* ========== Helper Methods ========== */

	var isSelected = function(obj) {
		return obj.data('selectedToAccount') == true || obj.data('selectedFromAccount') == true;
	}

	var isToSelected = function(obj) {
		return obj.data('selectedToAccount') == true;
	}

	var isFromSelected = function(obj) {
		return obj.data('selectedFromAccount') == true;
	}

	var resetToData = function() {
		$(".account").filter(function() {
			return $(this).data("selectedToAccount") == true
		}).data("selectedToAccount", false);
	}

	var resetFromData = function() {
		$(".account").filter(function() {
			return $(this).data("selectedFromAccount") == true
		}).data("selectedFromAccount", false);
	}

	/* ========== CSS Helper Library ========== */

	var selectingAccountsCss = {
		'border-style': 'solid',
		'border-color': '#b94a48',
		'border-width': '5px'
	}

	var selectedToAccountCss = {
		'border-style': 'solid',
		'border-color': 'green',
		'border-width': '5px'
	}

	var selectedFromAccountCss = {
		'border-style': 'solid',
		'border-color': 'black',
		'border-width': '5px'
	}

	var emptyBorder = {
		'border-style': '',
		'border-color': '',
		'border-width': ''	
	}

});