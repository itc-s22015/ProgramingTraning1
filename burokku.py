class Block:
    def __init__(self,canvas):
        self.cv = canvas
        self.w_x = 100 #ブロックの幅(x座標)
        self.w_y = 30 #ブロックの幅(y座標)
        
        self.id = self.cv.create_rectangle(350, 150, 150, 100, fill= "orange" )
'''
        #ブロックのスイッチ。1がON,0がOFF
        block_list =[[1,1,1,1,1,1,1,1,1,1,1,1], # j S= 0 , i = 0 ~ 11
                     [1,1,1,1,1,1,1,1,1,1,1,1], # j = 1 , i = 0 ~ 11
                     [1,1,1,1,1,1,1,1,1,1,1,1]] # j = 2 , i = 0 ~ 11 行・列の順番
        #def draw(self):
        for i in range(6):
            for j in range(3):
                self.cv.create_rectangle(i*self.w_x, j*self.w_y, (i+1)*self.w_x, (j+1)*self.w_y, fill = "orange", tag = "block"+str(j)+str(i))

        def reflect(self):
            for i in range(12):
                for j in range(3):
                    #ボールが上から反射
                    if (ball.y-ball.w < (j+1)*self.w_y #ボールがブロックよりも下
                        and i*self.w_x < ball.x < (i+1)*self.w_x #ボールがブロックの左右に挟まれている
                        and self.block_list[j][i] == 1): #スイッチが1
                            ball.dy *= -1 #反射させる
                            cv.delete("block"+str(j)+str(i)) #ブロックの描画を消す
                            self.block_list[j][i] = 0 #スイッチを切る
                            score.score += 1 #スコアの加点
                            score.delete() #スコアを更新（削除-生成)
                            score.draw()
'''