<?php
/**
 * Created by PhpStorm.
 * User: 程龙飞
 * Date: 2018/1/20
 * Time: 21:26
 */
class Data{
    private $mysqli;
    /**
     * Data constructor.
     * 初始化数据库
     */
    function __construct()
    {
        $this->mysqli = new mysqli("127.0.0.1","root","root",'lagou');
        if(mysqli_connect_errno()){
            exit(mysqli_connect_error());
        }
        $this->mysqli->set_charset("utf8");
    }

    /**
     * @return mixed    出现的次数
     */
    function get_type_num(){
        $sql = "SELECT count(*),type from data GROUP BY type";
        $data = $this->mysqli->query($sql);
        $arr = array();
        $num = 0 ;
        if($data){
            while ($da = $data->fetch_array()){
                $arr[$num]['value'] = $da[0];
                $arr[$num]['name'] = $da[1];
                $num++;
            }
        }else{
            exit("获取数据失败");
        }
        return $arr;
    }

    /**
     * 获取城市出现频率
     */
    function get_city_num(){
        $sql = "SELECT count(*) AS num ,city from data GROUP BY city ORDER BY num DESC LIMIT 0,18";
        $data = $this->mysqli->query($sql);
        $arr = array();
        $num = 0 ;
        if($data){
            while ($da = $data->fetch_array()){
                $arr[$num]['value'] = $da[0];
                $arr[$num]['name'] = $da[1];
                $num++;
            }
        }else{
            exit("获取数据失败");
        }
        return $arr;
    }

    /**
     * 生成图片
     */
    function get_photo($num = 20){
        $sql = "select companyLabelList from data";
        $data = $this->mysqli->query($sql);
        $arr = array();
        $str = '';

        if($data){
            while ($da = $data->fetch_array()){
                $str = @substr($da[0],1, strlen($da)-1);
                if($str){
                    foreach (explode( ',',$str) as $val){
                        if($val!='\'"\''){
                            $arr[] = trim($val);
                        }
                    };
                }
            }
        }else{
            exit("获取数据失败");
        }

        $arr1= array_count_values($arr);
        arsort($arr1);
        return array_slice($arr1,0,$num);
    }

    /**
     * 组织数据
     */
    function send_photo_data(){
        $arr_data = $this->get_photo();
        $arr = array();
        $num = 0;
        

        foreach ($arr_data as $key => $val){
            $arr[$num]['name'] = $key;
            $arr[$num]['value'] = (int)$val;
            $num ++;
        }
        
        return json_encode($arr);
    }

    function install_data($arr){
        foreach ($arr as $key => $val){

        }
    }
    function __destruct()
    {
        $this->mysqli->close();
        // TODO: Implement __destruct() method.
    }
}



