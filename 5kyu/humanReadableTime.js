//Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

//HH = hours, padded to 2 digits, range: 00 - 99
//MM = minutes, padded to 2 digits, range: 00 - 59
//SS = seconds, padded to 2 digits, range: 00 - 59
//The maximum time never exceeds 359999 (99:59:59)

function humanReadable (seconds) {
    let hours = parseInt(seconds/3600);
    let minutes = parseInt((seconds - hours*3600)/60);
    if (minutes == 60) {
      minutes = 0
    }
    
    let secondsDisp = parseInt(seconds-hours*3600-minutes*60)
    if (secondsDisp == 60) {
      secondsDisp = 0
    }
    let hoursStr = hours.toString();
    let minutesStr = minutes.toString();
    let secondsStr = secondsDisp.toString();
    return hoursStr.padStart(2, '0')+':'+minutesStr.padStart(2, '0')+':'+secondsStr.padStart(2, '0')
  }