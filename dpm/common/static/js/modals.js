document.addEventListener('DOMContentLoaded', (event) => {
    const openModalBtns = Array.from(document.querySelectorAll(".btn-open"));
    const overlays = Array.from(document.querySelectorAll(".overlay"));
    const closeModalBtns = Array.from(document.querySelectorAll(".btn-close"));

    const closeModal = function (modal, overlay) {
        modal.classList.add("hidden");
        overlay.classList.add("hidden");
    };

    closeModalBtns.forEach(function (btn) {
        btn.addEventListener("click", function (e) {
            const modalId = e.target.getAttribute("modal-btn-id");
            const modal = document.querySelector(`.modal[modal-id='${modalId}']`);
            const overlay = document.querySelector(`.overlay[modal-id='${modalId}']`);

            closeModal(modal, overlay);
        });
    });

    overlays.forEach(function (overlay) {
        overlay.addEventListener("click", function (e) {
            const modalId = e.target.getAttribute("modal-id");
            const modal = document.querySelector(`.modal[modal-id='${modalId}']`);

            closeModal(modal, overlay);
        });
    });

    const openModal = function (modal, overlay) {
        modal.classList.remove("hidden");
        overlay.classList.remove("hidden");
    };

    openModalBtns.forEach(function (btn) {
        btn.addEventListener("click", function (e) {
            const modalId = e.target.getAttribute("modal-btn-id");
            const modal = document.querySelector(`.modal[modal-id='${modalId}']`);
            const overlay = document.querySelector(`.overlay[modal-id='${modalId}']`);

            openModal(modal, overlay);
        });
    });
});
