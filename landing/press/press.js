document.querySelectorAll(".copybtn").forEach(function (btn) {
  btn.addEventListener("click", function () {
    var body = btn.closest(".copyblock").querySelector(".body");
    function done() { btn.textContent = "Copied"; setTimeout(function () { btn.textContent = "Copy"; }, 1400); }
    function select() { var r = document.createRange(); r.selectNodeContents(body); var s = getSelection(); s.removeAllRanges(); s.addRange(r); }
    if (navigator.clipboard) navigator.clipboard.writeText(body.textContent).then(done, select); else select();
  });
});
