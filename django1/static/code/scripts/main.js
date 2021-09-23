function previewFile() {
    const snapUrl = document.getElementById('snap_url');
    const snapThumb = document.getElementById('snap_thumb');
    const snap = document.getElementById('snap')
    const file = snap.files[0];
    const reader = new FileReader();
      reader.addEventListener("load", function () {
        snapThumb.src = reader.result;
        snapUrl.value = String(reader.result);
      }, false);
      if (file) {
        reader.readAsDataURL(file);
      }
}

const Launch = async () => {
    const selectReturnTimeDay = document.getElementById('selectReturnTimeDay')
    const selectReturnTimeDuration = document.getElementById('selectReturnTimeDuration')
    const sectionReturnTimeDay = document.getElementById('sectionReturnTimeDay')
    const sectionReturnTimeDuration = document.getElementById('sectionReturnTimeDuration')
    const leavingSchedule = document.getElementById('leavingSchedule')
    const snap = document.getElementById('snap')
    snap.onchange = previewFile;

    const date = new Date();
    leavingSchedule.value = `${date.getFullYear()}-${date.getMonth() < 10 ? "0" : ""}${date.getMonth()}` +
        `-${date.getDate() < 10 ? "0" : ""}${date.getDate()}T${date.getHours()}:${date.getMinutes()}`;
    selectReturnTimeDay.onclick = () => {
        sectionReturnTimeDay.style.display = ""
        sectionReturnTimeDuration.style.display = "none"
    }

    selectReturnTimeDuration.onclick = () => {
        sectionReturnTimeDay.style.display = "none"
        sectionReturnTimeDuration.style.display = "flex"
    }
}

window.onload = Launch;