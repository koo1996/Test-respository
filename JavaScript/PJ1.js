<script th:inline="javascript">
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

    let target = document.getElementsByClassName('card-date');
        for(let o of target){
            o.textContent = elapsedTime(o.getAttribute('data-created_datetime'));
        }
        console.log(target)
        function elapsedTime(date) {
            const start = new Date(date);
            const end = new Date();

            const diff = (end - start) / 1000;

            const times = [
                { name: '년', milliSeconds: 60 * 60 * 24 * 365 },
                { name: '개월', milliSeconds: 60 * 60 * 24 * 30 },
                { name: '일', milliSeconds: 60 * 60 * 24 },
                { name: '시간', milliSeconds: 60 * 60 },
                { name: '분', milliSeconds: 60 },
            ];

            for (const value of times) {
                const betweenTime = Math.floor(diff / value.milliSeconds);

                if (betweenTime > 0) {
                return `${betweenTime}${value.name} 전`;
                }
            }
            return '방금 전';
        }
    
</script>