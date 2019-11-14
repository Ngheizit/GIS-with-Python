using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Windows.Forms;
using System.Diagnostics;

namespace WeiboStat
{
    class MyUtils
    {
        public static string Info = "";

        /// <summary>
        /// 运行Python脚本
        /// </summary>
        /// <param name="filename">Python脚本绝对路径</param>
        /// <param name="args"></param>
        /// <param name="teps">脚本参数</param>
        public static void RunPy(string filename, string args = "", params string[] teps)
        {
            Info = "";


            string sArguments = filename;
            foreach (string sigstr in teps)
            {
                sArguments += " " + sigstr;//传递参数
            }
            sArguments += " " + args;

            ProcessStartInfo startInfo = new ProcessStartInfo() {
                FileName = "python.exe",
                Arguments = sArguments,
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardInput = true,
                RedirectStandardError = true,
                CreateNoWindow = true
            };
            Process p = new Process() {
                StartInfo = startInfo
            };
            p.Start();
            p.BeginOutputReadLine();
            p.OutputDataReceived += new DataReceivedEventHandler(OutputInfo);
            p.WaitForExit();
        }

        // 输出打印信息
        private static void OutputInfo(object sender, DataReceivedEventArgs e)
        {
            if (!string.IsNullOrEmpty(e.Data))
            {
                Info += e.Data + Environment.NewLine;
            }
        }



    }
}
