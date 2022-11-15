alert("real")

function uwu() {
    self = document.getElementById("clickme")
    if(self.value == "click me uwu"){
        alert("uwu")
        document.getElementById("clickme").value = ("loooool kys now")
    }else if(self.value == "loooool kys now"){
        alert("no really")
        document.getElementById("clickme").value = ("there is nothing left")
    }else if(self.value == "there is nothing left"){
        alert("stop")
        document.getElementById("clickme").value = ("do NOT click")
    }else if(self.value == "do NOT click"){
        alert("fine, i will unexist then")
        document.getElementById("clickme").remove()
    }
}