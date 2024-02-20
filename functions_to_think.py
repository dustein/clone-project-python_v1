create_job (userOwnerId: string, jobDescription: object) {
  const jobId = JOB#${new UILD()};

  await dynamodb.put({
    Entity: "Job", // PK do GSI_1
    id: jobId, // PK principal da tabela
    userOwnerId,
    // GSI_1_SK: undefined // não precisa adicionar se vazio
    ...jobDescription
  })
}

create_user (accountId: string, userDescription: object) {
  const userId = USER#${new UILD()};
  
  await dynamodb.put({
    Entity: "User", // PK do GSI_1
    id: userId, // PK principal da tabela
    accountId,
    GSI_1_SK: accountId,
    ...userDescription
  })
}