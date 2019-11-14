namespace WeiboStat
{
    partial class FormMain
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要修改
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.btn_SelectExcel = new System.Windows.Forms.Button();
            this.tbx_ExcelData = new System.Windows.Forms.TextBox();
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabPage1 = new System.Windows.Forms.TabPage();
            this.btn_CatchCN = new System.Windows.Forms.Button();
            this.btn_Result_CatchCN = new System.Windows.Forms.Button();
            this.tbx_Result_CatchCN = new System.Windows.Forms.TextBox();
            this.tabPage2 = new System.Windows.Forms.TabPage();
            this.btn_SelectStopWord = new System.Windows.Forms.Button();
            this.tbx_stopword = new System.Windows.Forms.TextBox();
            this.tbx_SelectSpiltDelWordTxt = new System.Windows.Forms.TextBox();
            this.btn_Select_Result_CatchCN = new System.Windows.Forms.Button();
            this.btn_Result_SplitDelWord = new System.Windows.Forms.Button();
            this.tbx_Result_SplitDelWord = new System.Windows.Forms.TextBox();
            this.btn_Run_SplitDelWord = new System.Windows.Forms.Button();
            this.tabPage3 = new System.Windows.Forms.TabPage();
            this.tabPage4 = new System.Windows.Forms.TabPage();
            this.tabPage5 = new System.Windows.Forms.TabPage();
            this.tabPage6 = new System.Windows.Forms.TabPage();
            this.tabPage7 = new System.Windows.Forms.TabPage();
            this.button2 = new System.Windows.Forms.Button();
            this.tbx_SelevtSpiltDel = new System.Windows.Forms.TextBox();
            this.button3 = new System.Windows.Forms.Button();
            this.tbx_Result_IDA = new System.Windows.Forms.TextBox();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.tbx_SelevtSpiltDel2 = new System.Windows.Forms.TextBox();
            this.button6 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.tbx_IDA = new System.Windows.Forms.TextBox();
            this.button8 = new System.Windows.Forms.Button();
            this.tbx_Result_docTopic = new System.Windows.Forms.TextBox();
            this.btn_Run_docTopic = new System.Windows.Forms.Button();
            this.button9 = new System.Windows.Forms.Button();
            this.tbx_SelevtSpiltDel3 = new System.Windows.Forms.TextBox();
            this.button10 = new System.Windows.Forms.Button();
            this.tbx_picture = new System.Windows.Forms.TextBox();
            this.button11 = new System.Windows.Forms.Button();
            this.button12 = new System.Windows.Forms.Button();
            this.tbx_SelevtSpiltDel4 = new System.Windows.Forms.TextBox();
            this.button13 = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.numericUpDown_passes = new System.Windows.Forms.NumericUpDown();
            this.label2 = new System.Windows.Forms.Label();
            this.numericUpDown_topic = new System.Windows.Forms.NumericUpDown();
            this.label3 = new System.Windows.Forms.Label();
            this.numericUpDown_word = new System.Windows.Forms.NumericUpDown();
            this.tabControl1.SuspendLayout();
            this.tabPage1.SuspendLayout();
            this.tabPage2.SuspendLayout();
            this.tabPage3.SuspendLayout();
            this.tabPage4.SuspendLayout();
            this.tabPage5.SuspendLayout();
            this.tabPage6.SuspendLayout();
            this.tabPage7.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_passes)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_topic)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_word)).BeginInit();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 271);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(464, 254);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // btn_SelectExcel
            // 
            this.btn_SelectExcel.Location = new System.Drawing.Point(6, 6);
            this.btn_SelectExcel.Name = "btn_SelectExcel";
            this.btn_SelectExcel.Size = new System.Drawing.Size(208, 29);
            this.btn_SelectExcel.TabIndex = 2;
            this.btn_SelectExcel.Text = "选择需要提取的微博数据（Excel）";
            this.btn_SelectExcel.UseVisualStyleBackColor = true;
            this.btn_SelectExcel.Click += new System.EventHandler(this.Btn_SelectExcel_Click);
            // 
            // tbx_ExcelData
            // 
            this.tbx_ExcelData.Location = new System.Drawing.Point(6, 41);
            this.tbx_ExcelData.Name = "tbx_ExcelData";
            this.tbx_ExcelData.ReadOnly = true;
            this.tbx_ExcelData.Size = new System.Drawing.Size(444, 21);
            this.tbx_ExcelData.TabIndex = 3;
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.tabPage1);
            this.tabControl1.Controls.Add(this.tabPage2);
            this.tabControl1.Controls.Add(this.tabPage3);
            this.tabControl1.Controls.Add(this.tabPage7);
            this.tabControl1.Controls.Add(this.tabPage4);
            this.tabControl1.Controls.Add(this.tabPage6);
            this.tabControl1.Controls.Add(this.tabPage5);
            this.tabControl1.Location = new System.Drawing.Point(12, 12);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(464, 252);
            this.tabControl1.TabIndex = 4;
            // 
            // tabPage1
            // 
            this.tabPage1.Controls.Add(this.btn_CatchCN);
            this.tabPage1.Controls.Add(this.btn_Result_CatchCN);
            this.tabPage1.Controls.Add(this.tbx_Result_CatchCN);
            this.tabPage1.Controls.Add(this.tbx_ExcelData);
            this.tabPage1.Controls.Add(this.btn_SelectExcel);
            this.tabPage1.Location = new System.Drawing.Point(4, 22);
            this.tabPage1.Name = "tabPage1";
            this.tabPage1.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage1.Size = new System.Drawing.Size(456, 226);
            this.tabPage1.TabIndex = 0;
            this.tabPage1.Text = "提取中文";
            this.tabPage1.UseVisualStyleBackColor = true;
            // 
            // btn_CatchCN
            // 
            this.btn_CatchCN.Location = new System.Drawing.Point(375, 129);
            this.btn_CatchCN.Name = "btn_CatchCN";
            this.btn_CatchCN.Size = new System.Drawing.Size(75, 27);
            this.btn_CatchCN.TabIndex = 5;
            this.btn_CatchCN.Text = "执行脚本";
            this.btn_CatchCN.UseVisualStyleBackColor = true;
            this.btn_CatchCN.Click += new System.EventHandler(this.Btn_CatchCN_Click_1);
            // 
            // btn_Result_CatchCN
            // 
            this.btn_Result_CatchCN.Location = new System.Drawing.Point(6, 68);
            this.btn_Result_CatchCN.Name = "btn_Result_CatchCN";
            this.btn_Result_CatchCN.Size = new System.Drawing.Size(208, 28);
            this.btn_Result_CatchCN.TabIndex = 4;
            this.btn_Result_CatchCN.Text = "选择结果数据路径";
            this.btn_Result_CatchCN.UseVisualStyleBackColor = true;
            this.btn_Result_CatchCN.Click += new System.EventHandler(this.Btn_CatchCN_Click);
            // 
            // tbx_Result_CatchCN
            // 
            this.tbx_Result_CatchCN.Location = new System.Drawing.Point(6, 102);
            this.tbx_Result_CatchCN.Name = "tbx_Result_CatchCN";
            this.tbx_Result_CatchCN.ReadOnly = true;
            this.tbx_Result_CatchCN.Size = new System.Drawing.Size(444, 21);
            this.tbx_Result_CatchCN.TabIndex = 3;
            // 
            // tabPage2
            // 
            this.tabPage2.Controls.Add(this.btn_Run_SplitDelWord);
            this.tabPage2.Controls.Add(this.btn_Result_SplitDelWord);
            this.tabPage2.Controls.Add(this.btn_SelectStopWord);
            this.tabPage2.Controls.Add(this.tbx_Result_SplitDelWord);
            this.tabPage2.Controls.Add(this.tbx_stopword);
            this.tabPage2.Controls.Add(this.tbx_SelectSpiltDelWordTxt);
            this.tabPage2.Controls.Add(this.btn_Select_Result_CatchCN);
            this.tabPage2.Location = new System.Drawing.Point(4, 22);
            this.tabPage2.Name = "tabPage2";
            this.tabPage2.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage2.Size = new System.Drawing.Size(456, 226);
            this.tabPage2.TabIndex = 1;
            this.tabPage2.Text = "分词与去除停用词";
            this.tabPage2.UseVisualStyleBackColor = true;
            // 
            // btn_SelectStopWord
            // 
            this.btn_SelectStopWord.Location = new System.Drawing.Point(6, 68);
            this.btn_SelectStopWord.Name = "btn_SelectStopWord";
            this.btn_SelectStopWord.Size = new System.Drawing.Size(208, 28);
            this.btn_SelectStopWord.TabIndex = 8;
            this.btn_SelectStopWord.Text = "选择停用词文件";
            this.btn_SelectStopWord.UseVisualStyleBackColor = true;
            this.btn_SelectStopWord.Click += new System.EventHandler(this.btn_SelectStopWord_Click);
            // 
            // tbx_stopword
            // 
            this.tbx_stopword.Location = new System.Drawing.Point(7, 102);
            this.tbx_stopword.Name = "tbx_stopword";
            this.tbx_stopword.ReadOnly = true;
            this.tbx_stopword.Size = new System.Drawing.Size(443, 21);
            this.tbx_stopword.TabIndex = 7;
            // 
            // tbx_SelectSpiltDelWordTxt
            // 
            this.tbx_SelectSpiltDelWordTxt.Location = new System.Drawing.Point(7, 41);
            this.tbx_SelectSpiltDelWordTxt.Name = "tbx_SelectSpiltDelWordTxt";
            this.tbx_SelectSpiltDelWordTxt.ReadOnly = true;
            this.tbx_SelectSpiltDelWordTxt.Size = new System.Drawing.Size(443, 21);
            this.tbx_SelectSpiltDelWordTxt.TabIndex = 7;
            // 
            // btn_Select_Result_CatchCN
            // 
            this.btn_Select_Result_CatchCN.Location = new System.Drawing.Point(6, 6);
            this.btn_Select_Result_CatchCN.Name = "btn_Select_Result_CatchCN";
            this.btn_Select_Result_CatchCN.Size = new System.Drawing.Size(208, 28);
            this.btn_Select_Result_CatchCN.TabIndex = 6;
            this.btn_Select_Result_CatchCN.Text = "选择【提取中文】结果数据";
            this.btn_Select_Result_CatchCN.UseVisualStyleBackColor = true;
            this.btn_Select_Result_CatchCN.Click += new System.EventHandler(this.Btn_Select_Result_CatchCN_Click);
            // 
            // btn_Result_SplitDelWord
            // 
            this.btn_Result_SplitDelWord.Location = new System.Drawing.Point(6, 129);
            this.btn_Result_SplitDelWord.Name = "btn_Result_SplitDelWord";
            this.btn_Result_SplitDelWord.Size = new System.Drawing.Size(208, 28);
            this.btn_Result_SplitDelWord.TabIndex = 9;
            this.btn_Result_SplitDelWord.Text = "选择结果输出路径";
            this.btn_Result_SplitDelWord.UseVisualStyleBackColor = true;
            this.btn_Result_SplitDelWord.Click += new System.EventHandler(this.Btn_Result_SplitDelWord_Click);
            // 
            // tbx_Result_SplitDelWord
            // 
            this.tbx_Result_SplitDelWord.Location = new System.Drawing.Point(7, 163);
            this.tbx_Result_SplitDelWord.Name = "tbx_Result_SplitDelWord";
            this.tbx_Result_SplitDelWord.ReadOnly = true;
            this.tbx_Result_SplitDelWord.Size = new System.Drawing.Size(443, 21);
            this.tbx_Result_SplitDelWord.TabIndex = 7;
            // 
            // btn_Run_SplitDelWord
            // 
            this.btn_Run_SplitDelWord.Location = new System.Drawing.Point(375, 190);
            this.btn_Run_SplitDelWord.Name = "btn_Run_SplitDelWord";
            this.btn_Run_SplitDelWord.Size = new System.Drawing.Size(75, 28);
            this.btn_Run_SplitDelWord.TabIndex = 10;
            this.btn_Run_SplitDelWord.Text = "执行脚本";
            this.btn_Run_SplitDelWord.UseVisualStyleBackColor = true;
            this.btn_Run_SplitDelWord.Click += new System.EventHandler(this.Btn_Run_SplitDelWord_Click);
            // 
            // tabPage3
            // 
            this.tabPage3.Controls.Add(this.numericUpDown_word);
            this.tabPage3.Controls.Add(this.label3);
            this.tabPage3.Controls.Add(this.numericUpDown_topic);
            this.tabPage3.Controls.Add(this.label2);
            this.tabPage3.Controls.Add(this.numericUpDown_passes);
            this.tabPage3.Controls.Add(this.label1);
            this.tabPage3.Controls.Add(this.button4);
            this.tabPage3.Controls.Add(this.tbx_Result_IDA);
            this.tabPage3.Controls.Add(this.tbx_SelevtSpiltDel);
            this.tabPage3.Controls.Add(this.button3);
            this.tabPage3.Controls.Add(this.button2);
            this.tabPage3.Location = new System.Drawing.Point(4, 22);
            this.tabPage3.Name = "tabPage3";
            this.tabPage3.Size = new System.Drawing.Size(456, 226);
            this.tabPage3.TabIndex = 2;
            this.tabPage3.Text = "应用IDA";
            this.tabPage3.UseVisualStyleBackColor = true;
            // 
            // tabPage4
            // 
            this.tabPage4.Controls.Add(this.btn_Run_docTopic);
            this.tabPage4.Controls.Add(this.tbx_Result_docTopic);
            this.tabPage4.Controls.Add(this.tbx_IDA);
            this.tabPage4.Controls.Add(this.button8);
            this.tabPage4.Controls.Add(this.button7);
            this.tabPage4.Location = new System.Drawing.Point(4, 22);
            this.tabPage4.Name = "tabPage4";
            this.tabPage4.Size = new System.Drawing.Size(456, 226);
            this.tabPage4.TabIndex = 3;
            this.tabPage4.Text = "主题统计";
            this.tabPage4.UseVisualStyleBackColor = true;
            // 
            // tabPage5
            // 
            this.tabPage5.Controls.Add(this.button13);
            this.tabPage5.Controls.Add(this.tbx_SelevtSpiltDel4);
            this.tabPage5.Controls.Add(this.button12);
            this.tabPage5.Location = new System.Drawing.Point(4, 22);
            this.tabPage5.Name = "tabPage5";
            this.tabPage5.Size = new System.Drawing.Size(456, 226);
            this.tabPage5.TabIndex = 4;
            this.tabPage5.Text = "词频";
            this.tabPage5.UseVisualStyleBackColor = true;
            // 
            // tabPage6
            // 
            this.tabPage6.Controls.Add(this.button11);
            this.tabPage6.Controls.Add(this.tbx_picture);
            this.tabPage6.Controls.Add(this.tbx_SelevtSpiltDel3);
            this.tabPage6.Controls.Add(this.button10);
            this.tabPage6.Controls.Add(this.button9);
            this.tabPage6.Location = new System.Drawing.Point(4, 22);
            this.tabPage6.Name = "tabPage6";
            this.tabPage6.Size = new System.Drawing.Size(456, 226);
            this.tabPage6.TabIndex = 5;
            this.tabPage6.Text = "绘制词云";
            this.tabPage6.UseVisualStyleBackColor = true;
            // 
            // tabPage7
            // 
            this.tabPage7.Controls.Add(this.button6);
            this.tabPage7.Controls.Add(this.tbx_SelevtSpiltDel2);
            this.tabPage7.Controls.Add(this.button5);
            this.tabPage7.Location = new System.Drawing.Point(4, 22);
            this.tabPage7.Name = "tabPage7";
            this.tabPage7.Size = new System.Drawing.Size(456, 226);
            this.tabPage7.TabIndex = 6;
            this.tabPage7.Text = "TFIDF";
            this.tabPage7.UseVisualStyleBackColor = true;
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(6, 6);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(208, 28);
            this.button2.TabIndex = 0;
            this.button2.Text = "选择【分词与去除停用词】结果数据";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.Button2_Click);
            // 
            // tbx_SelevtSpiltDel
            // 
            this.tbx_SelevtSpiltDel.Location = new System.Drawing.Point(6, 40);
            this.tbx_SelevtSpiltDel.Name = "tbx_SelevtSpiltDel";
            this.tbx_SelevtSpiltDel.ReadOnly = true;
            this.tbx_SelevtSpiltDel.Size = new System.Drawing.Size(443, 21);
            this.tbx_SelevtSpiltDel.TabIndex = 8;
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(6, 67);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(208, 28);
            this.button3.TabIndex = 0;
            this.button3.Text = "选择结果输出路径";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.Button3_Click);
            // 
            // tbx_Result_IDA
            // 
            this.tbx_Result_IDA.Location = new System.Drawing.Point(6, 101);
            this.tbx_Result_IDA.Name = "tbx_Result_IDA";
            this.tbx_Result_IDA.ReadOnly = true;
            this.tbx_Result_IDA.Size = new System.Drawing.Size(443, 21);
            this.tbx_Result_IDA.TabIndex = 8;
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(374, 128);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(75, 28);
            this.button4.TabIndex = 9;
            this.button4.Text = "执行脚本";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.Button4_Click);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(5, 6);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(208, 28);
            this.button5.TabIndex = 11;
            this.button5.Text = "选择【分词与去除停用词】结果数据";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.Button5_Click);
            // 
            // tbx_SelevtSpiltDel2
            // 
            this.tbx_SelevtSpiltDel2.Location = new System.Drawing.Point(5, 40);
            this.tbx_SelevtSpiltDel2.Name = "tbx_SelevtSpiltDel2";
            this.tbx_SelevtSpiltDel2.ReadOnly = true;
            this.tbx_SelevtSpiltDel2.Size = new System.Drawing.Size(443, 21);
            this.tbx_SelevtSpiltDel2.TabIndex = 12;
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(373, 67);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(75, 28);
            this.button6.TabIndex = 13;
            this.button6.Text = "执行脚本";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.Button6_Click);
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(3, 6);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(208, 28);
            this.button7.TabIndex = 15;
            this.button7.Text = "选择【应用IDA】结果数据";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.Button7_Click);
            // 
            // tbx_IDA
            // 
            this.tbx_IDA.Location = new System.Drawing.Point(3, 40);
            this.tbx_IDA.Name = "tbx_IDA";
            this.tbx_IDA.ReadOnly = true;
            this.tbx_IDA.Size = new System.Drawing.Size(443, 21);
            this.tbx_IDA.TabIndex = 16;
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(3, 67);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(208, 28);
            this.button8.TabIndex = 15;
            this.button8.Text = "选择数据结果数据";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.Button8_Click);
            // 
            // tbx_Result_docTopic
            // 
            this.tbx_Result_docTopic.Location = new System.Drawing.Point(3, 101);
            this.tbx_Result_docTopic.Name = "tbx_Result_docTopic";
            this.tbx_Result_docTopic.ReadOnly = true;
            this.tbx_Result_docTopic.Size = new System.Drawing.Size(443, 21);
            this.tbx_Result_docTopic.TabIndex = 16;
            // 
            // btn_Run_docTopic
            // 
            this.btn_Run_docTopic.Location = new System.Drawing.Point(371, 128);
            this.btn_Run_docTopic.Name = "btn_Run_docTopic";
            this.btn_Run_docTopic.Size = new System.Drawing.Size(75, 27);
            this.btn_Run_docTopic.TabIndex = 17;
            this.btn_Run_docTopic.Text = "执行脚本";
            this.btn_Run_docTopic.UseVisualStyleBackColor = true;
            this.btn_Run_docTopic.Click += new System.EventHandler(this.Btn_Run_docTopic_Click);
            // 
            // button9
            // 
            this.button9.Location = new System.Drawing.Point(3, 6);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(208, 28);
            this.button9.TabIndex = 14;
            this.button9.Text = "选择【分词与去除停用词】结果数据";
            this.button9.UseVisualStyleBackColor = true;
            this.button9.Click += new System.EventHandler(this.Button9_Click);
            // 
            // tbx_SelevtSpiltDel3
            // 
            this.tbx_SelevtSpiltDel3.Location = new System.Drawing.Point(3, 40);
            this.tbx_SelevtSpiltDel3.Name = "tbx_SelevtSpiltDel3";
            this.tbx_SelevtSpiltDel3.ReadOnly = true;
            this.tbx_SelevtSpiltDel3.Size = new System.Drawing.Size(443, 21);
            this.tbx_SelevtSpiltDel3.TabIndex = 17;
            // 
            // button10
            // 
            this.button10.Location = new System.Drawing.Point(3, 67);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(208, 28);
            this.button10.TabIndex = 14;
            this.button10.Text = "选择输出图片规格模板";
            this.button10.UseVisualStyleBackColor = true;
            this.button10.Click += new System.EventHandler(this.Button10_Click);
            // 
            // tbx_picture
            // 
            this.tbx_picture.Location = new System.Drawing.Point(3, 101);
            this.tbx_picture.Name = "tbx_picture";
            this.tbx_picture.ReadOnly = true;
            this.tbx_picture.Size = new System.Drawing.Size(443, 21);
            this.tbx_picture.TabIndex = 17;
            // 
            // button11
            // 
            this.button11.Location = new System.Drawing.Point(371, 128);
            this.button11.Name = "button11";
            this.button11.Size = new System.Drawing.Size(75, 27);
            this.button11.TabIndex = 19;
            this.button11.Text = "执行脚本";
            this.button11.UseVisualStyleBackColor = true;
            this.button11.Click += new System.EventHandler(this.Button11_Click);
            // 
            // button12
            // 
            this.button12.Location = new System.Drawing.Point(3, 6);
            this.button12.Name = "button12";
            this.button12.Size = new System.Drawing.Size(208, 27);
            this.button12.TabIndex = 15;
            this.button12.Text = "选择【分词与去除停用词】结果数据";
            this.button12.UseVisualStyleBackColor = true;
            this.button12.Click += new System.EventHandler(this.Button12_Click);
            // 
            // tbx_SelevtSpiltDel4
            // 
            this.tbx_SelevtSpiltDel4.Location = new System.Drawing.Point(3, 39);
            this.tbx_SelevtSpiltDel4.Name = "tbx_SelevtSpiltDel4";
            this.tbx_SelevtSpiltDel4.ReadOnly = true;
            this.tbx_SelevtSpiltDel4.Size = new System.Drawing.Size(443, 21);
            this.tbx_SelevtSpiltDel4.TabIndex = 16;
            // 
            // button13
            // 
            this.button13.Location = new System.Drawing.Point(371, 66);
            this.button13.Name = "button13";
            this.button13.Size = new System.Drawing.Size(75, 27);
            this.button13.TabIndex = 17;
            this.button13.Text = "执行脚本";
            this.button13.UseVisualStyleBackColor = true;
            this.button13.Click += new System.EventHandler(this.Button13_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 138);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(65, 12);
            this.label1.TabIndex = 10;
            this.label1.Text = "迭代次数：";
            // 
            // numericUpDown_passes
            // 
            this.numericUpDown_passes.Location = new System.Drawing.Point(83, 134);
            this.numericUpDown_passes.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
            this.numericUpDown_passes.Name = "numericUpDown_passes";
            this.numericUpDown_passes.Size = new System.Drawing.Size(68, 21);
            this.numericUpDown_passes.TabIndex = 11;
            this.numericUpDown_passes.Value = new decimal(new int[] {
            20,
            0,
            0,
            0});
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(24, 165);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(53, 12);
            this.label2.TabIndex = 10;
            this.label2.Text = "主题数：";
            // 
            // numericUpDown_topic
            // 
            this.numericUpDown_topic.Location = new System.Drawing.Point(83, 161);
            this.numericUpDown_topic.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
            this.numericUpDown_topic.Name = "numericUpDown_topic";
            this.numericUpDown_topic.Size = new System.Drawing.Size(68, 21);
            this.numericUpDown_topic.TabIndex = 11;
            this.numericUpDown_topic.Value = new decimal(new int[] {
            20,
            0,
            0,
            0});
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 192);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(65, 12);
            this.label3.TabIndex = 10;
            this.label3.Text = "关键词数：";
            // 
            // numericUpDown_word
            // 
            this.numericUpDown_word.Location = new System.Drawing.Point(83, 188);
            this.numericUpDown_word.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
            this.numericUpDown_word.Name = "numericUpDown_word";
            this.numericUpDown_word.Size = new System.Drawing.Size(68, 21);
            this.numericUpDown_word.TabIndex = 11;
            this.numericUpDown_word.Value = new decimal(new int[] {
            50,
            0,
            0,
            0});
            // 
            // FormMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(486, 537);
            this.Controls.Add(this.tabControl1);
            this.Controls.Add(this.richTextBox1);
            this.Name = "FormMain";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.FormMain_Load);
            this.tabControl1.ResumeLayout(false);
            this.tabPage1.ResumeLayout(false);
            this.tabPage1.PerformLayout();
            this.tabPage2.ResumeLayout(false);
            this.tabPage2.PerformLayout();
            this.tabPage3.ResumeLayout(false);
            this.tabPage3.PerformLayout();
            this.tabPage4.ResumeLayout(false);
            this.tabPage4.PerformLayout();
            this.tabPage5.ResumeLayout(false);
            this.tabPage5.PerformLayout();
            this.tabPage6.ResumeLayout(false);
            this.tabPage6.PerformLayout();
            this.tabPage7.ResumeLayout(false);
            this.tabPage7.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_passes)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_topic)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_word)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button btn_SelectExcel;
        private System.Windows.Forms.TextBox tbx_ExcelData;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabPage1;
        private System.Windows.Forms.TabPage tabPage2;
        private System.Windows.Forms.Button btn_Result_CatchCN;
        private System.Windows.Forms.TextBox tbx_Result_CatchCN;
        private System.Windows.Forms.Button btn_CatchCN;
        private System.Windows.Forms.Button btn_Select_Result_CatchCN;
        private System.Windows.Forms.TextBox tbx_SelectSpiltDelWordTxt;
        private System.Windows.Forms.Button btn_SelectStopWord;
        private System.Windows.Forms.TextBox tbx_stopword;
        private System.Windows.Forms.Button btn_Result_SplitDelWord;
        private System.Windows.Forms.TextBox tbx_Result_SplitDelWord;
        private System.Windows.Forms.Button btn_Run_SplitDelWord;
        private System.Windows.Forms.TabPage tabPage3;
        private System.Windows.Forms.TabPage tabPage4;
        private System.Windows.Forms.TabPage tabPage6;
        private System.Windows.Forms.TabPage tabPage7;
        private System.Windows.Forms.TabPage tabPage5;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.TextBox tbx_Result_IDA;
        private System.Windows.Forms.TextBox tbx_SelevtSpiltDel;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.TextBox tbx_SelevtSpiltDel2;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.TextBox tbx_IDA;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Button btn_Run_docTopic;
        private System.Windows.Forms.TextBox tbx_Result_docTopic;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.TextBox tbx_SelevtSpiltDel3;
        private System.Windows.Forms.TextBox tbx_picture;
        private System.Windows.Forms.Button button10;
        private System.Windows.Forms.Button button11;
        private System.Windows.Forms.Button button13;
        private System.Windows.Forms.TextBox tbx_SelevtSpiltDel4;
        private System.Windows.Forms.Button button12;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.NumericUpDown numericUpDown_passes;
        private System.Windows.Forms.NumericUpDown numericUpDown_word;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.NumericUpDown numericUpDown_topic;
        private System.Windows.Forms.Label label2;
    }
}

