package org.apache.solr.search.function;

import java.io.IOException;
import java.util.Map;

import org.apache.lucene.index.AtomicReaderContext;
import org.apache.lucene.queries.function.FunctionValues;
import org.apache.lucene.queries.function.ValueSource;
import org.apache.lucene.queries.function.docvalues.DoubleDocValues;

/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

public class SimpleTfidfValueSource extends ValueSource{
  private ValueSource vs;
  public SimpleTfidfValueSource(ValueSource vs){
    this.vs = vs;
  }
  @Override
  public FunctionValues getValues(Map context, AtomicReaderContext readerContext)
      throws IOException {
    return new DoubleDocValues(vs) {     
      public String strVal(int doc){
        System.out.println("function query - "+vs.description());
        int b = Integer.parseInt(vs.description())+1;
        return ""+b;
      }
      @Override
      public double doubleVal(int doc) {
        return 0;
      }
    };
  }

  @Override
  public boolean equals(Object o) {
    return false;
  }

  @Override
  public int hashCode() {
    return 0;
  }

  @Override
  public String description() {
    return null;
  }
  
}
