public class SampleFile_2 {
    // フィールド変数
    private boolean answer;
    private char b;

    // メインメソッド
    public static void main(String[] args) {
        SampleFile_2 ve = new SampleFile_2();
        ve.evaluateVariables(true, "Reiwa");
    }

    // メソッド
    public void evaluateVariables(boolean x, char year) {
        // ローカル変数
        byte c = 10;
        short d = 20;
        int index = 30;
        float f = 3.14f;
        long g = 1000000L;
        double variable = 2.71828;
        Object obj = new Object();
        String str = "Sample";
        Exception t = new Exception("Error");

        // 一文字変数
        answer = x;
        b = year;

        // 出力
        System.out.println("変数 a: " + answer);
        System.out.println("変数 b: " + b);
        System.out.println("変数 c: " + c);
        System.out.println("変数 d: " + d);
        System.out.println("変数 index: " + index);
        System.out.println("変数 f: " + f);
        System.out.println("変数 g: " + g);
        System.out.println("変数 variable: " + variable);
        System.out.println("変数 obj: " + obj.toString());
        System.out.println("変数 str: " + str);
        System.out.println("変数 t: " + t.getMessage());

        // 配列
        int[] n = { 1, 2, 3, 4, 5 };
        for (int i = 0; i < n.length; i++) {
            System.out.println("n[" + i + "] = " + n[i]);
        }
    }
}