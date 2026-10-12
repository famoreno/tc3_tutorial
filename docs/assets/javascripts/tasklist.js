(() => {
  const storagePrefix = "tc3-tutorial:task-progress:v1:";
  const taskSelector =
    "li.task-list-item > input[type='checkbox'], li.task-list-item > p > input[type='checkbox']";

  function getTaskEntries() {
    const occurrences = new Map();

    return Array.from(document.querySelectorAll(taskSelector)).map((checkbox, index) => {
      const taskContent = checkbox.parentElement.cloneNode(true);
      taskContent.querySelectorAll("input, a").forEach((element) => element.remove());

      const label = taskContent.textContent.replace(/\s+/g, " ").trim() || `task-${index}`;
      const occurrence = occurrences.get(label) || 0;
      occurrences.set(label, occurrence + 1);

      return { checkbox, key: `${label}#${occurrence}` };
    });
  }

  function getStorageKey() {
    const pagePath = window.location.pathname.replace(/\/+$/, "") || "/";
    return `${storagePrefix}${pagePath}`;
  }

  function readProgress() {
    try {
      const progress = JSON.parse(localStorage.getItem(getStorageKey()) || "{}");
      return progress && typeof progress === "object" && !Array.isArray(progress)
        ? progress
        : {};
    } catch {
      return {};
    }
  }

  function restoreProgress() {
    const progress = readProgress();

    getTaskEntries().forEach(({ checkbox, key }) => {
      if (Object.prototype.hasOwnProperty.call(progress, key)) {
        checkbox.checked = progress[key] === true;
      }
    });
  }

  function saveProgress(event) {
    if (!(event.target instanceof HTMLInputElement) || !event.target.matches(taskSelector)) {
      return;
    }

    const progress = readProgress();
    getTaskEntries().forEach(({ checkbox, key }) => {
      progress[key] = checkbox.checked;
    });

    try {
      localStorage.setItem(getStorageKey(), JSON.stringify(progress));
    } catch {
      // Keep task lists usable if browser storage is unavailable.
    }
  }

  document.addEventListener("change", saveProgress);
  window.addEventListener("pageshow", restoreProgress);

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", restoreProgress, { once: true });
  } else {
    restoreProgress();
  }
})();
