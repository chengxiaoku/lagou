<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Python抓取拉勾网数据</title>
</head>
<body>
<!-- 为ECharts准备一个具备大小（宽高）的Dom -->
<div id="main" style="height:400px;width: 50%;float: left"></div>
<div id="main1" style="height:650px;width: 50%; float: right"></div>
<div id="main2" style="height:650px;width: 50%;"></div>
<?php
    include_once "database.php";
    $da =new Data();
    $arr = $da->get_type_num();
    $arr1 = $da->get_city_num();
    $json1 = json_encode($arr);
    $json2 = json_encode($arr1);
    $json3=$da->send_photo_data();

?>
</body>
<!-- ECharts单文件引入 -->
<script src="echarts-2.2.7/build/dist/echarts.js"></script>
<script type="text/javascript">

    function get_type_num(json1){
        var myArray=new Array()
        //获取编程语言的个数
        for (var i =0; i<json1.length;i++){
            myArray[i] = json1[i]['name']
        }
        return myArray;
    }


    // 路径配置
    require.config({
        paths: {
            echarts: 'echarts-2.2.7/build/dist'
        }
    });

    // 使用
    require(
            [
                'echarts',
                'echarts/chart/pie', // 使用饼状图就加载bar模块，按需加载
                'echarts/chart/funnel',
                'echarts/chart/wordCloud',
                //'echarts/chart/line',
                 //'echarts/chart/stack',
                //'echarts/chart/tiled',
                //'echarts/chart/force',
                //'echarts/chart/chord',
                // 'echarts/chart/bar',
                //'echarts/chart/funnel'

            ],
            function (ec) {
                var json1 = <?php echo $json1?>;
                var json2 = <?php echo $json2?>;
                var json3 = <?php echo $json3?>;
                for(var i = 0;i<json3.length;i++){
                    json3[i].itemStyle=createRandomItemStyle()
                }

                // 基于准备好的dom，初始化echarts图表
                var myChart = ec.init(document.getElementById('main'));
                var myChart1 = ec.init(document.getElementById('main1'));
                var myChart2 = ec.init(document.getElementById('main2'));

                var option = {
                    title : {
                        text: '编程语言出现频率',
                        subtext: '数据来自拉勾网',
                        x:'center'
                    },
                    tooltip : {
                        trigger: 'item',
                        formatter: "{a} <br/>{b} : {c} ({d}/次)"
                    },
                    legend: {
                        orient : 'vertical',
                        x : 'left',
                        data:get_type_num(json1)
                    },
                    toolbox: {
                        show : true,
                        feature : {
                            mark : {show: true},
                            dataView : {show: true, readOnly: false},
                            magicType : {
                                show: true,
                                type: ['pie', 'funnel'],
                                option: {
                                    funnel: {
                                        x: '25%',
                                        width: '20%',
                                        funnelAlign: 'left',
                                        max: 1548
                                    }
                                }
                            },
                            restore : {show: true},
                            saveAsImage : {show: true}
                        }
                    },
                    calculable : true,
                    series : [
                        {
                            name:'出现频率',
                            type:'pie',
                            radius : '55%',
                            center: ['50%', '60%'],
                            data:json1
                        }
                    ]
                };

                var option1 = {
                    title : {
                        text: '城市出现频率',
                        subtext: '数据来自拉勾网',
                        x:'right',
                        y:'bottom'
                    },
                    tooltip : {
                        trigger: 'item',
                        formatter: "{a} <br/>{b} : {c} ({d}%)"
                    },
                    legend: {
                        orient : 'vertical',
                        x : 'left',
                        data:get_type_num(json2)
                    },
                    toolbox: {
                        show : true,
                        feature : {
                            mark : {show: true},
                            dataView : {show: true, readOnly: false},
                            restore : {show: true},
                            saveAsImage : {show: true}
                        }
                    },
                    calculable : false,
                    series : (function (){
                        var series = [];
                        for (var i = 0; i < 30; i++) {
                            series.push({
                                name:'城市出现频率（来自拉勾网）',
                                type:'pie',
                                itemStyle : {normal : {
                                    label : {show : i > 28},
                                    labelLine : {show : i > 28, length:20}
                                }},
                                radius : [i * 4 + 40, i * 4 + 43],
                                data:json2
                            })
                        }
                        series[0].markPoint = {
                            symbol:'emptyCircle',
                            symbolSize:series[0].radius[0],
                            effect:{show:true,scaleSize:12,color:'rgba(250,225,50,0.8)',shadowBlur:10,period:30},
                            data:[{x:'50%',y:'50%'}]
                        };
                        return series;
                    })()
                };
                setTimeout(function (){
                    var _ZR = myChart.getZrender();
                    var TextShape = require('zrender/shape/Text');
                    // 补充千层饼
                    _ZR.addShape(new TextShape({
                        style : {
                            x : _ZR.getWidth() / 2,
                            y : _ZR.getHeight() / 2,
                            color: '#666',
                            text : '',
                            textAlign : 'center'
                        }
                    }));
                    _ZR.addShape(new TextShape({
                        style : {
                            x : _ZR.getWidth() / 2 + 200,
                            y : _ZR.getHeight() / 2,
                            brushType:'fill',
                            color: 'orange',
                            text : '',
                            textAlign : 'left',
                            textFont:'normal 20px 微软雅黑'
                        }
                    }));
                    _ZR.refresh();
                }, 2000);

                function createRandomItemStyle() {
                    return {
                        normal: {
                            color: 'rgb(' + [
                                Math.round(Math.random() * 160),
                                Math.round(Math.random() * 160),
                                Math.round(Math.random() * 160)
                            ].join(',') + ')'
                        }
                    };
                }

                option2 = {
                    title: {
                        text: '团队奖励',
                        link: 'http://www.google.com/trends/hottrends'
                    },
                    tooltip: {
                        show: true
                    },
                    series: [{
                        name: '团队奖励',
                        type: 'wordCloud',
                        size: ['80%', '80%'],
                        textRotation : [0, 45, 90, -45],
                        textPadding: 0,
                        autoSize: {
                            enable: true,
                            minSize: 14
                        },
                        data:json3
                    }]
                };

                // 为echarts对象加载数据
                myChart.setOption(option);
                myChart1.setOption(option1);
                myChart2.setOption(option2);
            }
    );



</script>
</html>