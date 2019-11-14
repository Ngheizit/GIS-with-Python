using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WeiboStat
{
    public partial class FormMain : Form
    {
        public FormMain()
        {
            InitializeComponent();
        }
        private void FormMain_Load(object sender, EventArgs e)
        {

        }

        #region 提取中文
        private void Btn_SelectExcel_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofg = new OpenFileDialog()
            {
                Title = "打开微博表格数据",
                Filter = "Excel表格 (*.xlsx)|*.xlsx"
            };
            if (ofg.ShowDialog() == DialogResult.OK)
            {
                tbx_ExcelData.Text = ofg.FileName;
            }
        }
        private void Btn_CatchCN_Click(object sender, EventArgs e)
        {
            SaveFileDialog sfg = new SaveFileDialog()
            {
                Title = "保存输出结果至",
                Filter = "文本 (*.txt)|*.txt"
            };
            if (sfg.ShowDialog() == DialogResult.OK)
            {
                tbx_Result_CatchCN.Text = sfg.FileName;
            }
        }
        private void Btn_CatchCN_Click_1(object sender, EventArgs e)
        {
            try
            {
                FormSchedule schedule = new FormSchedule(3);
                schedule.Show();

                schedule.GO("设置脚本参数"); // = 1
                string[] strArr = new string[2] {
                    tbx_ExcelData.Text, tbx_Result_CatchCN.Text
                };
                schedule.GO("运行脚本"); // = 2
                MyUtils.RunPy(Application.StartupPath + @"\wxz_1_提取中文.py", "", strArr);

                schedule.GO("信息打印"); // = 3
                richTextBox1.Text = MyUtils.Info;

                schedule.OK();
                tbx_SelectSpiltDelWordTxt.Text = tbx_Result_CatchCN.Text;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString(), "错误信息");
            }
        }
        #endregion

        #region 分词并去除停用词
        private void Btn_Select_Result_CatchCN_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofg = new OpenFileDialog()
            {
                Title = "打开【提取中文】结果数据",
                Filter = "文本 (*.txt)|*.txt"
            };
            if (ofg.ShowDialog() == DialogResult.OK)
            {
                tbx_SelectSpiltDelWordTxt.Text = ofg.FileName;
            }
        }
        private void btn_SelectStopWord_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofg = new OpenFileDialog()
            {
                Title = "打开停用词数据",
                Filter = "文本 (*.txt)|*.txt"
            };
            if (ofg.ShowDialog() == DialogResult.OK)
            {
                tbx_stopword.Text = ofg.FileName;
            }
        }
        private void Btn_Result_SplitDelWord_Click(object sender, EventArgs e)
        {
            SaveFileDialog sfg = new SaveFileDialog()
            {
                Title = "保存输出结果至",
                Filter = "文本 (*.txt)|*.txt"
            };
            if (sfg.ShowDialog() == DialogResult.OK)
            {
                tbx_Result_SplitDelWord.Text = sfg.FileName;
            }
        }
        private void Btn_Run_SplitDelWord_Click(object sender, EventArgs e)
        {
            try
            {
                FormSchedule schedule = new FormSchedule(3);
                schedule.Show();

                schedule.GO("参数设置");
                string[] strArr = new string[3] {
                    tbx_SelectSpiltDelWordTxt.Text, tbx_stopword.Text, tbx_Result_SplitDelWord.Text
                };

                schedule.GO("执行脚本");
                MyUtils.RunPy(Application.StartupPath + @"\wxz_2_分词并去除停用词.py", "", strArr);

                schedule.GO("打印信息");
                richTextBox1.Text = MyUtils.Info;

                schedule.OK();
                tbx_SelevtSpiltDel.Text = tbx_Result_SplitDelWord.Text;
                tbx_SelevtSpiltDel2.Text = tbx_Result_SplitDelWord.Text;
                tbx_SelevtSpiltDel3.Text = tbx_Result_SplitDelWord.Text;
                tbx_SelevtSpiltDel4.Text = tbx_Result_SplitDelWord.Text;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());
            }
        }
        #endregion

        #region 应用IDA
        private void Button2_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofg = new OpenFileDialog()
            {
                Title = "打开【分词并去除停用词】结果数据",
                Filter = "文本 (*.txt)|*.txt"
            };
            if (ofg.ShowDialog() == DialogResult.OK)
            {
                tbx_SelevtSpiltDel.Text = ofg.FileName;
            }
        }
        private void Button3_Click(object sender, EventArgs e)
        {
            SaveFileDialog sfg = new SaveFileDialog()
            {
                Title = "保存输出结果至",
                Filter = "文本 (*.txt)|*.txt"
            };
            if (sfg.ShowDialog() == DialogResult.OK)
            {
                tbx_Result_IDA.Text = sfg.FileName;
            }
        }
        private void Button4_Click(object sender, EventArgs e)
        {
            try
            {
                FormSchedule schedule = new FormSchedule(3);
                schedule.Show();

                schedule.GO("设置脚本参数"); // = 1
                string[] strArr = new string[5] {
                    tbx_SelevtSpiltDel.Text,
                    tbx_Result_IDA.Text,
                    numericUpDown_passes.Value.ToString(),
                    numericUpDown_topic.Value.ToString(),
                    numericUpDown_word.Value.ToString()
                };
                schedule.GO("运行脚本"); // = 2
                MyUtils.RunPy(Application.StartupPath + @"\wxz_3_应用IDA.py", "", strArr);

                schedule.GO("信息打印"); // = 3
                richTextBox1.Text = MyUtils.Info;

                schedule.OK();
                tbx_IDA.Text = tbx_Result_IDA.Text;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString(), "错误信息");
            }
        }
        #endregion

        #region TFIDF
        private void Button5_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofg = new OpenFileDialog()
            {
                Title = "打开【分词并去除停用词】结果数据",
                Filter = "文本 (*.txt)|*.txt"
            };
            if (ofg.ShowDialog() == DialogResult.OK)
            {
                tbx_SelevtSpiltDel2.Text = ofg.FileName;
            }
        }
        private void Button6_Click(object sender, EventArgs e)
        {
            try
            {
                FormSchedule schedule = new FormSchedule(3);
                schedule.Show();

                schedule.GO("设置脚本参数"); // = 1
                string[] strArr = new string[1] {
                    tbx_SelevtSpiltDel2.Text
                };
                schedule.GO("运行脚本"); // = 2
                MyUtils.RunPy(Application.StartupPath + @"\wxz_4_TFIDF.py", "", strArr);

                schedule.GO("信息打印"); // = 3
                richTextBox1.Text = MyUtils.Info;

                schedule.OK();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString(), "错误信息");
            }
        }
        #endregion

        #region 主题匹配
        private void Button7_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofg = new OpenFileDialog()
            {
                Title = "打开【应用IDA】结果数据",
                Filter = "文本 (*.txt)|*.txt"
            };
            if (ofg.ShowDialog() == DialogResult.OK)
            {
                tbx_IDA.Text = ofg.FileName;
            }
        }
        private void Button8_Click(object sender, EventArgs e)
        {
            SaveFileDialog sfg = new SaveFileDialog()
            {
                Title = "保存输出结果至",
                Filter = "文本 (*.txt)|*.txt"
            };
            if (sfg.ShowDialog() == DialogResult.OK)
            {
                tbx_Result_docTopic.Text = sfg.FileName;
            }
        }
        private void Btn_Run_docTopic_Click(object sender, EventArgs e)
        {
            try
            {
                FormSchedule schedule = new FormSchedule(3);
                schedule.Show();

                schedule.GO("设置脚本参数"); // = 1
                string[] strArr = new string[2] {
                    tbx_IDA.Text, tbx_Result_docTopic.Text
                };
                schedule.GO("运行脚本"); // = 2
                MyUtils.RunPy(Application.StartupPath + @"\wxz_5_主题分配.py", "", strArr);

                schedule.GO("信息打印"); // = 3
                richTextBox1.Text = MyUtils.Info;

                schedule.OK();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString(), "错误信息");
            }
        }
        #endregion

        #region 绘制词云
        private void Button9_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofg = new OpenFileDialog()
            {
                Title = "打开【分词并去除停用词】结果数据",
                Filter = "文本 (*.txt)|*.txt"
            };
            if (ofg.ShowDialog() == DialogResult.OK)
            {
                tbx_SelevtSpiltDel3.Text = ofg.FileName;
            }
        }
        private void Button10_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofg = new OpenFileDialog()
            {
                Title = "选择输出图片规格模板",
                Filter = "图片 (*.png)|*.png"
            };
            if (ofg.ShowDialog() == DialogResult.OK)
            {
                tbx_picture.Text = ofg.FileName;
            }
        }
        private void Button11_Click(object sender, EventArgs e)
        {
            try
            {
                FormSchedule schedule = new FormSchedule(3);
                schedule.Show();

                schedule.GO("设置脚本参数"); // = 1
                string[] strArr = new string[2] {
                    tbx_SelevtSpiltDel3.Text, tbx_picture.Text
                };
                schedule.GO("运行脚本"); // = 2
                MyUtils.RunPy(Application.StartupPath + @"\wxz_6_词云绘制.py", "", strArr);

                schedule.GO("信息打印"); // = 3
                richTextBox1.Text = MyUtils.Info;

                schedule.OK();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString(), "错误信息");
            }
        }
        #endregion

        #region 词频
        private void Button12_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofg = new OpenFileDialog()
            {
                Title = "打开【分词并去除停用词】结果数据",
                Filter = "文本 (*.txt)|*.txt"
            };
            if (ofg.ShowDialog() == DialogResult.OK)
            {
                tbx_SelevtSpiltDel4.Text = ofg.FileName;
            }
        }
        private void Button13_Click(object sender, EventArgs e)
        {
            try
            {
                FormSchedule schedule = new FormSchedule(3);
                schedule.Show();

                schedule.GO("设置脚本参数"); // = 1
                string[] strArr = new string[1] {
                    tbx_SelevtSpiltDel4.Text
                };
                schedule.GO("运行脚本"); // = 2
                MyUtils.RunPy(Application.StartupPath + @"\wxz_7_词频.py", "", strArr);

                schedule.GO("信息打印"); // = 3
                richTextBox1.Text = MyUtils.Info;

                schedule.OK();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString(), "错误信息");
            }
        } 
        #endregion
    }
}
