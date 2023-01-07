class DataStream {
public:
    int vt,kt , count;
    DataStream(int value, int k) {
        vt = value;
        kt = k;
        count = 0;
    }
    
    bool consec(int num) {
        if(num == vt)
        {
            count++;
        }
        else
            count = 0;
        return count>=kt;
    }
};

/**
 * Your DataStream object will be instantiated and called as such:
 * DataStream* obj = new DataStream(value, k);
 * bool param_1 = obj->consec(num);
 */
