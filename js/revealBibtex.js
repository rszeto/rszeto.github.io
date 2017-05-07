document.addEventListener("DOMContentLoaded", function() {
	var showBibtexDivs = document.getElementsByClassName("showBibtex");
	for(var i = 0; i < showBibtexDivs.length; i++) {
		(function() {
			var showBibtexDiv = showBibtexDivs[i];
			var showBibtexLink = showBibtexDiv.firstElementChild;
			var bibtexContent = showBibtexDiv.lastElementChild;
			showBibtexLink.addEventListener("click", function() {
				bibtexContent.style.display = (bibtexContent.style.display === "none" ? "block" : "none");
			})
		})()
	}
})
