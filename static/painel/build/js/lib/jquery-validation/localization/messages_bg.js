!function(e){"function"==typeof define&&define.amd?define(["jquery","../jquery.validate"],e):"object"==typeof module&&module.exports?module.exports=e(require("jquery")):e(jQuery)}(function(e){e.extend(e.validator.messages,{required:"Полето е задължително.",remote:"Моля, въведете правилната стойност.",email:"Моля, въведете валиден email.",url:"Моля, въведете валидно URL.",date:"Моля, въведете валидна дата.",dateISO:"Моля, въведете валидна дата (ISO).",number:"Моля, въведете валиден номер.",digits:"Моля, въведете само цифри.",creditcard:"Моля, въведете валиден номер на кредитна карта.",equalTo:"Моля, въведете същата стойност отново.",extension:"Моля, въведете стойност с валидно разширение.",maxlength:e.validator.format("Моля, въведете повече от {0} символа."),minlength:e.validator.format("Моля, въведете поне {0} символа."),rangelength:e.validator.format("Моля, въведете стойност с дължина между {0} и {1} символа."),range:e.validator.format("Моля, въведете стойност между {0} и {1}."),max:e.validator.format("Моля, въведете стойност по-малка или равна на {0}."),min:e.validator.format("Моля, въведете стойност по-голяма или равна на {0}.")})});