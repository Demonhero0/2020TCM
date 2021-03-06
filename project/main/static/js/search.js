(function () {
  const search_elem = document.getElementById("search");
  const search_text_elem = document.getElementById("search__input");
  const search_btn_elem = document.getElementById("search__button");

  const do_search = () => {
    const search_string = search_text_elem.value;
    if (search_string != null && search_string !== "") {
      document.location = `${
        document.location.origin
      }/api/check?content=${encodeURIComponent(search_text_elem.value)}`;
    }
  };

  window.addEventListener("load", () => {
    if (document.location.pathname === "/api/check") {
      const urlParams = new URLSearchParams(window.location.search);
      const searchString = urlParams.get("content");
      if (searchString !== null) {
        search_text_elem.value = searchString;
      }
    }
  });

  search_text_elem.addEventListener("focus", () => {
    search_elem.classList.add(["search--focus"]);
  });
  search_text_elem.addEventListener("blur", () => {
    search_elem.classList.remove(["search--focus"]);
  });
  search_text_elem.addEventListener("keypress", (ent) => {
    if (ent.key === "Enter") {
      do_search();
    }
  });
  search_btn_elem.addEventListener("click", () => {
    do_search();
  });
})();
