$("select[name=changeTest]").change(function(){
    console.log($(this).val()); //value값 가져오기
    let num = $(this).val()
    console.log($("select[name=changeTest] option:selected").text()); //text값 가져오기
    location.href = `/mainPage?value=${num}`
});

    $("select[name=keyword]").change(function(){
    console.log($(this).val());
    let num = $(this).val()
    console.log($("select[name=keyword] option:selected").text()); //text값 가져오기
    location.href = `/search?keyword=${num}`
});
