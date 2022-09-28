 def avaliacao(self):
        for gene in self.cromossomo:
                if gene == "L":
                    if self.pos[0] < 0 or self.pos[1]-1 < 0 or self.pos[0] > (self.tamanho_matriz-1) or self.pos[1]-1 > (self.tamanho_matriz - 1):
                        break

                    if self.maze[self.pos[0]][self.pos[1]-1] == '1':
                        break

                    if (self.pos[0], self.pos[1]-1) not in self.jaVisitado:
                        if self.maze[self.pos[0]][self.pos[1]-1] == '0':
                            self.nota_avaliacao += 2
                            self.pos = (self.pos[0], self.pos[1]-1)
                            self.jaVisitado.append((self.pos[0], self.pos[1]-1))


                        if self.maze[self.pos[0]][self.pos[1]-1] == 'C':
                            self.nota_avaliacao += 5
                            self.pos = (self.pos[0],self.pos[1]-1)
                            self.jaVisitado.append((self.pos[0],self.pos[1]-1))

                    if (self.pos[0],self.pos[1]-1) in self.jaVisitado:
                            self.nota_avaliacao -= 1
                            self.pos = (self.pos[0],self.pos[1]-1)
                            

                if gene == "R":
                    if self.pos[0] < 0 or self.pos[1]+1 < 0 or self.pos[0] > (self.tamanho_matriz-1) or self.pos[1]+1 > (self.tamanho_matriz -1): 
                        break
                        
                    if self.maze[self.pos[0]][self.pos[1]+1] == '1':
                        break
                        
                    if (self.pos[0],self.pos[1]+1) not in self.jaVisitado:
                                if self.maze[self.pos[0]][self.pos[1]+1] == '0':
                                    self.nota_avaliacao += 2
                                    self.pos = (self.pos[0],self.pos[1]+1)
                                    self.jaVisitado.append((self.pos[0],self.pos[1]+1))   

                                if self.maze[self.pos[0]][self.pos[1]+1] == 'C':
                                    self.nota_avaliacao += 5
                                    self.pos = (self.pos[0],self.pos[1]+1)
                                    self.jaVisitado.append((self.pos[0],self.pos[1]+1))

                    if (self.pos[0],self.pos[1]+1) in self.jaVisitado:
                                self.nota_avaliacao -= 1
                                self.pos = (self.pos[0],self.pos[1]+1)


                if gene == "UP":
                    if  self.pos[0]-1 < 0 or self.pos[1] < 0 or self.pos[0]-1 > (self.tamanho_matriz-1) or self.pos[1] > (self.tamanho_matriz -1): 
                        break
                        
                    if self.maze[self.pos[0]-1][self.pos[1]] == '1':
                        break 

                    if (self.pos[0]-1,self.pos[1]) not in self.jaVisitado:
                                if self.maze[self.pos[0]-1][self.pos[1]] == '0':
                                    self.nota_avaliacao += 2
                                    self.pos = (self.pos[0]-1,self.pos[1])
                                    self.jaVisitado.append((self.pos[0]-1,self.pos[1]))
                                
                                if self.maze[self.pos[0]-1][self.pos[1]] == 'C':
                                    self.nota_avaliacao += 5
                                    self.pos = (self.pos[0]-1,self.pos[1])
                                    self.jaVisitado.append((self.pos[0]-1,self.pos[1]))

                    if (self.pos[0]-1,self.pos[1]) in self.jaVisitado:
                                self.nota_avaliacao -= 1
                                self.pos = (self.pos[0]-1,self.pos[1])     

                if gene == "DOWN":
                    if  self.pos[0]+1 < 0 or self.pos[1] < 0 or self.pos[0]+1 > (self.tamanho_matriz-1) or self.pos[1] > (self.tamanho_matriz -1): 
                        break

                    if self.maze[self.pos[0]+1][self.pos[1]] == '1':
                        break

                    if (self.pos[0]+1,self.pos[1]) not in self.jaVisitado:
                                if self.maze[self.pos[0]+1][self.pos[1]] == '0':
                                    self.nota_avaliacao += 2 
                                    self.pos = (self.pos[0]+1,self.pos[1])
                                    self.jaVisitado.append((self.pos[0]+1,self.pos[1]))
                                
                                
                                if self.maze[self.pos[0]+1][self.pos[1]] == 'C':
                                    self.nota_avaliacao += 5
                                    self.pos = (self.pos[0]+1,self.pos[1])
                                    self.jaVisitado.append((self.pos[0]+1,self.pos[1]))

                    if (self.pos[0]+1,self.pos[1]) in self.jaVisitado: 
                                self.nota_avaliacao -= 1
                                self.pos = (self.pos[0]+1,self.pos[1])
                                
        
                if gene == "LUP":
                    if  self.pos[0]-1 < 0 or self.pos[1]-1 < 0 or self.pos[0]-1 > (self.tamanho_matriz-1) or self.pos[1]-1 > (self.tamanho_matriz -1): 
                        break
                        
                           
                    if self.maze[self.pos[0]-1][self.pos[1]-1] == '1':
                        break

                    if (self.pos[0]-1,self.pos[1]-1) not in self.jaVisitado:
                            if self.maze[self.pos[0]-1][self.pos[1]-1] == '0':
                                self.nota_avaliacao += 2 
                                self.pos = (self.pos[0]-1,self.pos[1]-1)
                                self.jaVisitado.append((self.pos[0]-1,self.pos[1]-1))
                                
                            if self.maze[self.pos[0]-1][self.pos[1]-1] == 'C':
                                self.nota_avaliacao += 5
                                self.pos = (self.pos[0]-1,self.pos[1]-1)
                                self.jaVisitado.append((self.pos[0]-1,self.pos[1]-1))

                    if (self.pos[0]-1,self.pos[1]-1) in self.jaVisitado:
                                self.nota_avaliacao -= 1
                                self.pos = (self.pos[0]-1,self.pos[1]-1)
                                
                   
                if gene == "RUP":
                    if  self.pos[0]-1 < 0 or self.pos[1]+1 < 0 or self.pos[0]-1 > (self.tamanho_matriz-1) or self.pos[1]+1 > (self.tamanho_matriz -1): 
                        break
                        
                    if self.maze[self.pos[0]-1][self.pos[1]+1] == '1':
                        break 
                           
                    if (self.pos[0]-1,self.pos[1]+1) not in self.jaVisitado:
                                if self.maze[self.pos[0]-1][self.pos[1]+1] == '0':
                                    self.nota_avaliacao += 2 
                                    self.pos = (self.pos[0]-1,self.pos[1]+1)
                                    self.jaVisitado.append((self.pos[0]-1,self.pos[1]+1))

                                if self.maze[self.pos[0]-1][self.pos[1]+1] == 'C':
                                    self.nota_avaliacao += 5
                                    self.pos = (self.pos[0]-1,self.pos[1]+1)
                                    self.jaVisitado.append((self.pos[0]-1,self.pos[1]+1))
                                
                    if (self.pos[0]-1,self.pos[1]+1) in self.jaVisitado:
                                self.nota_avaliacao -= 1
                                self.pos = (self.pos[0]-1,self.pos[1]+1)
                            
                   
                if gene == "LDOWN":
                    if  self.pos[0]+1 < 0 or self.pos[1]-1 < 0 or self.pos[0]+1 > (self.tamanho_matriz-1) or self.pos[1]-1 > (self.tamanho_matriz -1): 
                        break
                        
                    if self.maze[self.pos[0]+1][self.pos[1]-1] == '1':
                        break

                    if (self.pos[0]+1,self.pos[1]-1) not in self.jaVisitado:
                            if self.maze[self.pos[0]+1][self.pos[1]-1] == '0':
                                self.nota_avaliacao += 2
                                self.pos = (self.pos[0]+1,self.pos[1]-1)
                                self.jaVisitado.append((self.pos[0]+1,self.pos[1]-1))

                            if self.maze[self.pos[0]+1][self.pos[1]-1] == 'C':
                                self.nota_avaliacao += 5
                                self.pos = (self.pos[0]+1,self.pos[1]-1)
                                self.jaVisitado.append((self.pos[0]+1,self.pos[1]-1))
                            
                    if (self.pos[0]+1,self.pos[1]-1) in self.jaVisitado:
                                self.nota_avaliacao -= 1
                                self.pos = (self.pos[0]+1,self.pos[1]-1)
                        
                    
                if gene == "RDOWN":
                    if  self.pos[0]+1 < 0 or self.pos[1]+1 < 0 or self.pos[0]+1 > (self.tamanho_matriz-1) or self.pos[1]+1 > (self.tamanho_matriz-1): 
                        break
                       
                    if self.maze[self.pos[0]+1][self.pos[1]+1] == '1':
                        break

                    if (self.pos[0]+1,self.pos[1]+1) not in self.jaVisitado:
                            if self.maze[self.pos[0]+1][self.pos[1]+1] == '0':
                                self.nota_avaliacao += 2  
                                self.pos = (self.pos[0]+1,self.pos[1]+1)
                                self.jaVisitado.append((self.pos[0]+1,self.pos[1]+1))
                             
                            if self.maze[self.pos[0]+1][self.pos[1]+1] == 'C':
                                    self.nota_avaliacao += 5
                                    self.pos = (self.pos[0]+1,self.pos[1]+1) 
                                    self.jaVisitado.append((self.pos[0]+1,self.pos[1]+1))

                    if (self.pos[0]+1,self.pos[1]+1) in self.jaVisitado:
                                self.nota_avaliacao -= 1
                                self.pos = (self.pos[0]+1,self.pos[1]+1)