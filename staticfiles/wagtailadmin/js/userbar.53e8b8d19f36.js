document.addEventListener("DOMContentLoaded",(function(){var e=document.querySelector("[data-wagtail-userbar]"),t=e.querySelector("[data-wagtail-userbar-trigger]"),n=e.querySelector("[role=menu]"),r=n.querySelectorAll("li"),i="is-active";function a(r){e.classList.add(i),t.setAttribute("aria-expanded","true"),n.addEventListener("click",f,!1),window.addEventListener("click",m,!1),e.addEventListener("keydown",l,!1),r&&n.querySelector("a[href],\n    button:not([disabled]),\n    input:not([disabled])")&&setTimeout((function(){s()}),300)}function o(){e.classList.remove(i),t.setAttribute("aria-expanded","false"),n.addEventListener("click",f,!1),window.removeEventListener("click",m,!1),e.removeEventListener("keydown",l,!1)}function u(){r.forEach((function(e){e.firstElementChild.tabIndex=-1}))}function c(e){u(),e.tabIndex=0,setTimeout((function(){e.focus()}),100)}function s(){r.length>0&&c(r[0].firstElementChild)}function d(){r.length>0&&c(r[r.length-1].firstElementChild)}function l(e){if("true"===t.getAttribute("aria-expanded")){if("Escape"===e.key)return o(),setTimeout((function(){return t.focus()}),300),u(),!1;if(document.activeElement&&document.activeElement.closest(".wagtail-userbar-items"))switch(e.key){case"ArrowDown":return e.preventDefault(),r.forEach((function(e,t){e.firstElementChild===document.activeElement&&(t+1<r.length?c(r[t+1].firstElementChild):s())})),!1;case"ArrowUp":return e.preventDefault(),r.forEach((function(e,t){e.firstElementChild===document.activeElement&&(t>0?c(r[t-1].firstElementChild):d())})),!1;case"Home":return e.preventDefault(),s(),!1;case"End":return e.preventDefault(),d(),!1}}return!0}function f(e){e.stopPropagation()}function m(){o()}t.addEventListener("click",(function(t){t.stopPropagation(),e.classList.contains(i)?o():a(!0)}),!1),window.addEventListener("pageshow",o,!1),e.addEventListener("keydown",(function(e){if(t===document.activeElement&&"false"===t.getAttribute("aria-expanded"))switch(e.key){case"ArrowUp":e.preventDefault(),a(!1),setTimeout((function(){return d()}),300);break;case"ArrowDown":e.preventDefault(),a(!1),setTimeout((function(){return s()}),300)}})),n.addEventListener("focusout",(function(e){null==e.relatedTarget||e.relatedTarget&&e.relatedTarget.closest(".wagtail-userbar-items")||(u(),o())})),u()}));
//# sourceMappingURL=userbar.js.map